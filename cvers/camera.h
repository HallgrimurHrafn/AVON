#include <raspicam/raspicam_cv.h>
#include <opencv2/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

// Global variables
int min_H = 156;
int min_S = 144;
int min_V = 25;
int max_H = 182;
int max_S = 204;
int max_V = 255;
int const max_value = 255;
int const max_morph = 20;

cv::Mat img;
cv::Mat equ, hsv, mask;

cv::Scalar lowerb = cv::Scalar(min_H, min_S, min_V);
cv::Scalar upperb = cv::Scalar(max_H, max_S, max_V);

int erodeOn = 1;
int dilateOn = 1;

int erodeSize = 1;
int dilateSize = 7;

cv::Mat erodeElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(erodeSize+3,erodeSize+3) );
cv::Mat dilateElement = cv::getStructuringElement( cv::MORPH_RECT, cv::Size(dilateSize+3,dilateSize+3) );

vector<int> XYZ;
int X, Y, Z; // Stores center of marker, does not update unless a new position is found.
int detectCounter = 0;
bool detected = false;

//bool trackingOn = false;
//bool close = false;

void update_Var( int, void*);

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
			if (area > 800 && area < 25000) {
				detected = true;
				detectCounter = 10;
				Z = area;
				X = moment.m10/area;
				Y = moment.m01/area;
				X = (int) X*127/320 -1;
				Y = (int) Y*127/320 -1;
				Z = (int) sqrt(Z-800)*127/sqrt(25000-800);
			}
		}
	}
	if (detected) {
		detectCounter = detectCounter-1;
		if (detectCounter <= 0) {
			detected = false;
			detectCounter = 0;
		}
	}
	cout << detectCounter << endl;
}

void initialize() {
	raspicam::RaspiCam_Cv Camera;

	Camera.set(CV_CAP_PROP_FORMAT, CV_8UC3 ); // For color
	Camera.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	Camera.set(CV_CAP_PROP_FRAME_HEIGHT, 320);

	cout << "Opening camera..." << endl;

	if (!Camera.open()) {
		 cerr << "Error opening camera!" << endl;
	}
}

void terminate(){
	cout << "Stopping camera.." << endl;
	Camera.release();
}

vector<int> vision() {
	Camera.grab();
	Camera.retrieve(img);

	cv::cvtColor(img,img,CV_BGR2RGB);
	colorIsolation(img, hsv, mask);
	morphOps(mask);
	trackMarker(mask, img);

	if (detected) {
		XYZ[0] = 1;
		XYZ[1] = X;
		XYZ[2] = Y;
		XYZ[3] = Z;
	}
	else {
		XYZ[0] = 0;
	}
	return XYZ;
}
