#include <raspicam/raspicam_cv.h>
#include <opencv2/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

// g++ vision.cpp -shared -I/usr/include/python2.7/ -lpython2.7 -lboost_python -o vision.so
//TODO:
//1. normalisa XYZ
//2. laga main
//3. laga CMakeLists
//4. testa

using namespace std;

// Global variables
int min_H = 53;
int min_S = 0;
int min_V = 234;
int max_H = 147;
int max_S = 27;
int max_V = 255;
int const max_value = 255;
int const max_morph = 20;

cv::Scalar lowerb = cv::Scalar(min_H, min_S, min_V);
cv::Scalar upperb = cv::Scalar(max_H, max_S, max_V);

int erodeOn = 1;
int dilateOn = 1;

int erodeSize = 0;
int dilateSize = 0;

cv::Mat erodeElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(erodeSize+3,erodeSize+3) );
cv::Mat dilateElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(dilateSize+3,dilateSize+3) );

int X, Y, Z; // Stores center of marker, does not update unless a new position is found.
int detectCounter = 0;
bool detected = false;

//bool trackingOn = false;
//bool close = false;

void update_Var( int, void*);

// Initialize Trackbars for tuning
void createTrackbars() {
	cv::namedWindow("Options" , 0);

	cv::createTrackbar("min H", "Options", &min_H, max_value );
	cv::createTrackbar("max H", "Options", &max_H, max_value );
	cv::createTrackbar("min S", "Options", &min_S, max_value );
	cv::createTrackbar("max S", "Options", &max_S, max_value );
	cv::createTrackbar("min V", "Options", &min_V, max_value );
	cv::createTrackbar("max V", "Options", &max_V, max_value );

	cv::createTrackbar("Erode", "Options", &erodeOn, 1);
	cv::createTrackbar("Erode size", "Options", &erodeSize, max_morph, update_Var );
	cv::createTrackbar("Dilate", "Options", &dilateOn, 1);
	cv::createTrackbar("Dilate size", "Options", &dilateSize, max_morph, update_Var );
}

// Creates black and white mask image of certain HSV range, set with Options
void colorIsolation(cv::Mat &frame, cv::Mat &hsv, cv::Mat &mask) {
	cv::cvtColor( frame, hsv, CV_BGR2HSV );
	cv::inRange( hsv, cv::Scalar(min_H, min_S, min_V),
			  cv::Scalar(max_H, max_S, max_V), mask );
}

// Performs the morphological operations Erode and/or Dilate on a mask image.
void morphOps(cv::Mat &mask) {
	if(erodeOn)
		cv::erode(mask, mask, erodeElement);
	if(dilateOn)
		cv::dilate(mask, mask, dilateElement);
}

void trackMarker(cv::Mat binaryImg, cv::Mat &frame) {
	vector< vector<cv::Point> > contours;
	vector<cv::Vec4i> hierarchy;

	cv::Mat temp = binaryImg;

	cv::findContours(temp, contours, hierarchy, CV_RETR_TREE , CV_CHAIN_APPROX_NONE);

	if (hierarchy.size() > 0) {
		int numObjects = hierarchy.size();
		for (int i=0; i>=0; i = hierarchy[i][0]){
			cv::Moments moment = cv::moments((cv::Mat)contours[i]);
			int area = moment.m00;
			if (area > 200) {
				detected = true;
				detectCounter = 10;
				Z = area;
				X = moment.m10/area;
				Y = moment.m01/area;
				cout << X << Y << Z << endl;
			}
		}
	}
	if (detected) {
		detectCounter = detectCounter--;
		if (detectCounter <= 0) {
			detected = false;
			detectCounter = 0;
		}
	}
}

int main(int argc, char **argv) {
	raspicam::RaspiCam_Cv Camera;

	cv::Mat img;
	cv::Mat equ, hsv, mask;

	Camera.set(CV_CAP_PROP_FORMAT, CV_8UC3 ); // For color
	Camera.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	Camera.set(CV_CAP_PROP_FRAME_HEIGHT, 320);

	cout << "Opening camera..." << endl;

	if (!Camera.open()) {
		 cerr << "Error opening camera!" << endl;
 		return -1;
 	}
	
	cout << "1" << endl;
	
	cv::namedWindow("Tracker", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("HSV", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Mask", cv::WINDOW_AUTOSIZE);
	
	cout << "1" << endl;

	createTrackbars();
	update_Var(0, 0);
	
	cout << "1" << endl;

	for (;;) {
		Camera.grab();
		Camera.retrieve(img);

		cv::cvtColor(img,img,CV_BGR2RGB);
		colorIsolation(img, hsv, mask);
		cv::imshow("HSV", hsv);
		morphOps(mask);
		cv::imshow("Mask", mask);
		trackMarker(mask, img);

		// Display image	
		cv::imshow("Tracker", img);
	
		if (cv::waitKey(1)==27) {
			break;
		}
	}
	cout << "Stopping camera.." << endl;
	Camera.release();

	return 0;
}

// Update global variables
void update_Var( int, void*) {
	erodeElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(erodeSize+3,erodeSize+3 ) );
    dilateElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(dilateSize+3,dilateSize+3) );
}
