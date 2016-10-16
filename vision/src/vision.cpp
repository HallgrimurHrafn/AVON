#include <raspicam/raspicam_cv.h>
#include <opencv2/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

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

int x[3], y[3];
int centerX, centerY; // Stores center of marker, does not update unless a new position is found.

cv::Scalar lowerb = cv::Scalar(min_H, min_S, min_V);
cv::Scalar upperb = cv::Scalar(max_H, max_S, max_V);

int erodeOn = 1;
int dilateOn = 1;

int erodeSize;
int dilateSize;

cv::Mat erodeElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(erodeSize,erodeSize) );
cv::Mat dilateElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(dilateSize,dilateSize) );

int freeze = 1;

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
	
	cv::createTrackbar("Still", "Options", &freeze, 1);
}

// Equalize histogram of frame
void equalizeIntensity(cv::Mat &frame, cv::Mat &equ){
	cv::Mat ycrcb;
	cv::cvtColor( frame, ycrcb, CV_BGR2YCrCb);
	
	vector<cv::Mat> channels;
	cv::split(ycrcb,channels);
	
	cv::equalizeHist(channels[0],channels[0]);
	
	cv::merge(channels,ycrcb);
	
	cv::cvtColor(ycrcb, equ, CV_YCrCb2BGR);
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

void drawMarker(int x, int y, cv::Mat &img, cv::Scalar color) {
}

void trackMarker(cv::Mat binaryImg, cv::Mat &frame) {
	vector< vector<cv::Point> > contours;
	vector<cv::Vec4i> hierarchy;
	
	cv::Mat temp = binaryImg;
	
	cv::findContours(temp, contours, hierarchy, CV_RETR_TREE , CV_CHAIN_APPROX_NONE);
	
	cv::drawContours(frame, contours, -1, cv::Scalar(0,0,255), 1, 8, hierarchy);
}

int main(int argc, char **argv) {
	// Live playback
	raspicam::RaspiCam_Cv Camera;
	//
	
	// Video playback
	//cv::VideoCapture video("malbiksol.avi");
	//

	cv::Mat img;
	cv::Mat frame, equ, hsv, mask;
	
	// Set camera parameters for Live playback
	Camera.set(CV_CAP_PROP_FORMAT, CV_8UC3 ); // For color
	Camera.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	Camera.set(CV_CAP_PROP_FRAME_HEIGHT, 320);
	//
	
	// Open camera
	cout << "Opening camera..." << endl;

    
	if (!Camera.open()) {
		 		cerr << "Error opening camera!" << endl; 
 		return -1; 
 	}
 	
	cv::namedWindow("Tracker", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("HSV", cv::WINDOW_AUTOSIZE);
	//cv::namedWindow("Equalized",cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Mask", cv::WINDOW_AUTOSIZE);
	
	createTrackbars();
	update_Var(0, 0);

	for (;;) {		
		Camera.grab();
		Camera.retrieve(img);
		
		cv::cvtColor(img,img,CV_BGR2RGB);

		
		//equalizeIntensity(img,equ);
		//cv::imshow("Equalized",equ);
		
		colorIsolation(img, hsv, mask);
		//cv::imshow("HSV", hsv);
		
		morphOps(mask);
		cv::imshow("Mask", mask);	
		
		// Display image
		cv::imshow("Tracker", img);
		
		if (cv::waitKey(1) == 27){
			break;
		}
	}
	cout << "Stopping camera.." << endl;
	// Live playback
	Camera.release();
	//

	return 0;
}

// Update global variables
void update_Var( int, void*) {
	erodeElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(erodeSize+3,erodeSize+3 ) );
    dilateElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(dilateSize+3,dilateSize+3) );
}
