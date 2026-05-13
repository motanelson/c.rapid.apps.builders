heads_="""
//gcc games.c -o game -lSDL2 -lm
#include <SDL2/SDL.h>
#include "SDLs.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#define True 1;
#define False 0;
#define true 1;
#define false 0;

int score=0;
int fire=0;
int live=0;
int lives=3;
int x=0;
int y=0;
int z=0;
int w=0;
int h=0;
int ends=False;
int camera=0;
int enemy=0;
int enemycount=3;
SDL_Window *window ;
SDL_Renderer *renderer;
SDL_Texture *texture;
int running = 1;
SDL_Event event;

#define tsleep 100000
void debugs(char *c){
    printf("%s\\n",c);
    usleep(tsleep);
}

"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()


def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value):
    print("handle : function :"+value)
    
    saves(files,"a","void ")
    saves(files,"a",value)
    saves(files,"a"," (){\n")
    saves(files,"a",(" "*4)+"//put you code here\n")
    saves(files,"a",(" "*4)+ "debugs(\"")
    saves(files,"a",value)
    saves(files,"a","\");\n}\n")

print(filesa)
gfiles=getfiles(filesa)

filesa=filesa.replace(".txt",".c")
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)


heads__="""
    int mainloop(){
    //put you code here
    debugs("mainloop");
    while(running){
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = 0;
            }
        }


"""

def defs_(files,value):
    print("handle : function :"+value)
    saves(files,"a","\n"+" "*12)
    
    saves(files,"a",value)
    saves(files,"a","();\n")

saves(filesa,"a",heads__)

for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs_(filesa,sss)

heads___="""
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        SDL_RenderPresent(renderer);
        if (ends)return ends;
    }
    return ends;
}

int setuploop(){
    //put you code here
    debugs("setuploop");
    while(running){
       if (mainloop())return ends;
    }
    
    
    // Cleanup
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return ends;
}
int main(int argc,char *argv[]){
    //put you code here
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("SDL_Init Error: %s\\n", SDL_GetError());
        return 1;
    }

    window = SDL_CreateWindow("256 Colors", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        printf("SDL_CreateWindow Error: %s\\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }


    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        printf("SDL_CreateRenderer Error: %s\\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Create a texture to render the 256 colors
    texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGB332, SDL_TEXTUREACCESS_STREAMING, WIDTH, HEIGHT);
    if (!texture) {
        printf("SDL_CreateTexture Error: %s\\n", SDL_GetError());
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }
    clears(0,0,0);
    SDL_UpdateTexture(texture, NULL, screen, WIDTH);
    debugs("main");
    setuploop();

    return 0;
}
"""
saves(filesa,"a",heads___)