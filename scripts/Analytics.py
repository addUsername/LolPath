import cv2
import json
import os.path

class Analytics:
    
    champions = []
    champions_name = []
    champions_dict={}
    
    scale_percent = 52 # percent of original size
    
    title = ""
    
    def __init__(self,video_path,champions):
        
        self.video_path=video_path
        print(self.video_path + " Searching ")
        self.champions_name=champions
        self.champions = []
        for name in champions:
            self.champions_dict[name]=[]
        
        
    def getChampions(self):
        
        print("loading resources: "+self.champions_name[0])
        for champi in self.champions_name:
            print(os.getcwd()[:len(os.getcwd())-13]+"visualization\\resources\\"+champi+".jpg")
            champ = cv2.imread(os.getcwd()[:len(os.getcwd())-13]+"visualization\\resources\\"+champi+".jpg")
            dim = self.resizeChampion(champ.shape)
            row=dim[0]
            col=dim[1]
            champ = cv2.resize(champ, (col,row), interpolation = cv2.INTER_NEAREST)
            
            champ = cv2.GaussianBlur(champ, (5,5),0)
            champ  = cv2.cvtColor(champ, cv2.COLOR_BGR2GRAY)
            champ  = cv2.Canny(champ, 50,100,True)
            self.champions.append(champ)
        
    def resizeChampion(self, shape):
        return [int(shape[1] * self.scale_percent / 100), int(shape[0] * self.scale_percent / 100)]
    
    def readVideo(self, threshold, second_inicial, frame_step, frame_stop):
        
        self.getChampions()
        self.title+="threshold"+str(threshold)+"_noCNN34"
        h_champ ,w_champ = self.champions[0].shape
        
        video_rgb = cv2.VideoCapture(self.video_path)
        video_rgb.set(cv2.CAP_PROP_POS_FRAMES, int((second_inicial*30)))
        #video_rgb.set(cv2.CAP_PROP_POS_FRAMES, 2000)
        
        
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
                    if (fram_pos<frame_stop):
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
                                self.champions_dict[self.champions_name[i]].append([max_loc[0]+int(w_champ/2),max_loc[1]+int(h_champ/2)])
                            else:
                                self.champions_dict[self.champions_name[i]].append(None)
                            i+=1
                        i=0
                    elif (fram_pos>frame_stop):
                        self.champions_dict["0frameStep"]=frame_step
                        self.champions_dict["0seg,f_step,f_stop"]=[second_inicial, frame_step, frame_stop]
                        print(self.champions_dict["0seg,f_step,f_stop"])
                        self.writeJSON()
                        return 1                    
                        
                    fram_pos+=1
            else:
                break
        print("Lenght of first champion: "+str(len(self.champions_dict[self.champions_name[0]])))
        print("Printing json: ..\\outputs\\"+self.title+"2.json")
        self.champions_dict["0frameStep"]=frame_step
        self.champions_dict["0seg,f_step,f_stop"]=[second_inicial, frame_step, frame_stop]
        self.writeJSON()

    def writeVideo(self,jsonName):
                        
        self.title = jsonName
        self.readJson()
        self.champions_name = [name for name in self.champions_dict.keys() if "0" not in name]
        print(self.champions_name)
        colors=[(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)] #red,green,blue,yellow
        
        fram_pos=0
        ult_valid_position = [tuple((0,1)) for i in range (5)]
        
        
        video_rgb = cv2.VideoCapture(self.video_path)
        video_rgb.set(cv2.CAP_PROP_POS_FRAMES, int((self.champions_dict["0seg,f_step,f_stop"][0]*30)))
        #video_rgb.set(cv2.CAP_PROP_POS_FRAMES, 2000)
        _, frame = video_rgb.read()
        
        h = frame.shape[0]
        w = frame.shape[1]
        h1 = int(h - h/4)
        w1 = int(w - w/7)
        frame = frame[h1:h,w1:w]
        print(frame.shape[1],frame.shape[0])
        
                
        print("escribiendo video")
        print("Wirttin"+str(self.champions_dict[self.champions_name[3]][fram_pos]))
        print((self.video_path[:-4]+self.title+'.avi'))
        
        out = cv2.VideoWriter(self.video_path[:-4]+self.title+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (frame.shape[1],frame.shape[0]))
        while(video_rgb.isOpened()):

            ret, frame = video_rgb.read()
            if ((ret == True) and (fram_pos<self.champions_dict["0seg,f_step,f_stop"][2])):
                
                frame = frame[h1:h,w1:w]
                if(fram_pos%self.champions_dict["0seg,f_step,f_stop"][1]==0):
                    i=0
                    for champ in (self.champions):
                       position  = self.champions_dict[self.champions_name[i]][fram_pos]
                       if(position != None):
                           ult_valid_position[i]=[position[0],position[1]]
                           cv2.circle(frame,tuple((ult_valid_position[i])), 13, colors[i], 1)
                       else:
                           cv2.circle(frame,tuple((ult_valid_position[i])), 13, colors[i], 1)
                       i+=1
                else:
                    i=0
                    for champ in (self.champions):
                        cv2.circle(frame,tuple((ult_valid_position[i])), 13, colors[i], 1)
                        i+=1
                fram_pos+=1
                out.write(frame)                    
            else:
                break

        out.release()
        print("video escrito")
        
    def writeJSON(self):
        
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","w") as file: 
            json.dump(self.champions_dict, file)
            
    def readJson(self):
        #Asi nos saltamos tener q analizar el video, lo pillamos de aqui e ya.
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","r") as file:
            self.champions_dict = json.load(file)
            #print(self.champions_dict)

    
    
   
    
    
    
    
    
    
        