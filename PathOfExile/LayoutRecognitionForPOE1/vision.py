import cv2  as cv
import numpy as np

class Vision:
    seek_img=None
    seek_img_h=0
    seek_img_w=0
    method=None

    def __init__(self, seek_img_path, method=cv.TM_CCOEFF_NORMED):
        self.seek_img = cv.imread(seek_img_path, cv.IMREAD_REDUCED_COLOR_2,)
        self.seek_img_h=self.seek_img.shape[0]
        self.seek_img_w=self.seek_img.shape[1]
        self.method=method
    def find(self ,screen_img,treshhold=0.75,debug_mode=None):
        
        result=cv.matchTemplate(screen_img, self.seek_img, self.method)
        locations=np.where(result>=treshhold)
        locations=list(zip(*locations[::-1]))

        rectangles=[]
        for loc in locations:
            rect=[int(loc[0]), int(loc[1]), self.seek_img_w, self.seek_img_h]
            rectangles.append(rect)
            rectangles.append(rect)
        rectangles, weights =cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points=[]
        if len(rectangles):
            line_color=(0,255,0)
            line_type=cv.LINE_4
            marker_color=(255,0,255)
            marker_type=cv.MARKER_CROSS
            for(x,y,w,h) in rectangles:
                center_x=x+int(w/2)
                center_y=y+int(h/2)
                points.append((center_x,center_y))

                if debug_mode == 'rectangles':
                    top_left=(x,y)
                    bottom_right=(x+w,y+h)
                    cv.rectangle(screen_img, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)
                elif debug_mode == 'points':
                    cv.drawMarker(screen_img, (center_x,center_y), color=marker_color, markerType=marker_type,
                                markerSize=10, thickness=2, line_type=line_type)
        if debug_mode:
            cv.imshow('Matches', screen_img)
        return points