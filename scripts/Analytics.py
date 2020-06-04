import cv2
import json

class Analytics:
    
    champions = []
    champions_name = []
    champions_path={}
    frame_step=0
    
    scale_percent = 52 # percent of original size
    
    title = ""
    
    def __init__(self,video_path,champions):
        
        self.video_path=video_path
        self.champions_name=champions
        self.champions = []
        for name in champions:
            self.champions_path[name]=[]
        self.getChampions()
        
    def getChampions(self):
        
        for champi in self.champions_name:
            
            champ = cv2.imread(champi)
            dim = self.resizeChampion(champ.shape)
            champ = cv2.resize(champ, dim, interpolation = cv2.INTER_NEAREST)
            
            champ = cv2.GaussianBlur(champ, (5,5),0)
            champ  = cv2.cvtColor(champ, cv2.COLOR_BGR2GRAY)
            champ  = cv2.Canny(champ, 50,100,True)
            self.champions.append(champ)
        
    def resizeChampion(self, shape):
        return [int(shape[1] * self.scale_percent / 100), int(shape[0] * self.scale_percent / 100)]
    
    def readVideo(self, threshold, second_inicial, frame_step):
        
        self.title+="threshold_"+str(threshold)
        self.frame_step=frame_step
        h_champ ,w_champ = self.champions[0].shape
        
        video_rgb = cv2.VideoCapture(self.video_path)
        video_rgb.set(cv2.CAP_PROP_POS_FRAMES, (second_inicial*30)-1)
        
        _, frame = video_rgb.read()
        #select portion image
        h = frame.shape[0]
        w = frame.shape[1]
        h1 = int(h-h/4)
        w1 = int(w - w/7)
        
        fram_pos=0
        while(video_rgb.isOpened()):
            
            ret, frame = video_rgb.read()
            
            if ret == True:
                
                if (fram_pos%frame_step==0):
                
                    #crop map area
                    frame = frame[h1:h,w1:w]
            
                    #frame transformation
                    frame = cv2.GaussianBlur(frame,(5,5),0)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = cv2.Canny(frame,50,100,True)
                    
                    i=0
                    for champ in (self.champions):
                        #frame_compare = cv2.subtract(frame_canny,start)
                        res = cv2.matchTemplate(frame,champ,cv2.TM_CCOEFF_NORMED)
                        _, max_val, _, max_loc = cv2.minMaxLoc(res)
                        if(max_val > threshold):
                            self.champion_paths[self.champions_name[i]].append([max_loc[0]+int(w_champ/2),max_loc[1]+int(h_champ/2)])
                        else:
                            self.champion_paths[self.champions_name[i]].append(None)
                        i+=1
                    i=0
                fram_pos+=1
            else:
                break
        
            
    def writeVideo(self):
        #falta hacer la lectura desde el json y no desde el atributo champios_path
        video=[]
        colors=[(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)] #red,green,blue,yellow
        video_rgb = cv2.VideoCapture(self.video_path)
        
        first = iter(self.champions_path[0])
        second = iter(self.champions_path[1])
        third = iter(self.champions_path[2])
        fourth = iter(self.champions_path[3])
        fifth = iter(self.champions_path[4])
        
        iterators = [first,second,third,fourth,fifth]
        
        _, frame = video_rgb.read()
        
        h = frame.shape[0]
        w = frame.shape[1]
        h1 = int(h - h/4)
        w1 = int(w - w/7)
        
        fram_pos=0
        
        print("escribiendo video")
        while(video_rgb.isOpened()):

            ret, frame = video_rgb.read()
            if ret == True:
                if (fram_pos%self.frame_step==0):
                    frame = frame[h1:h,w1:w]
                    i=0
                    for champ in (self.champions):
                       position  = next(iterators[i])
                       if(position!=None):
                           cv2.circle(frame,(position[1],position[0]), 5, colors[i], -1)
                       i+=1
                    i=0
                    video.append(frame)
                fram_pos=0
            else:
                break
        
        out = cv2.VideoWriter('..\\outputs\\videos\\'+self.title+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (video[0].shape[1],video[1].shape[0]))
        for i in range(len(video)):
            out.write(video[i])
        out.release()
        print("video escrito")
        
        