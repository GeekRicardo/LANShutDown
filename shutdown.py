# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:36:48 2019

@author: Ricardo
"""
import platform
import os

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shutdownnow')
def shutdownnow():
    try:
        p = getplatform()
        if p==1:
            os.system('shutdown -s -t 1')
        elif p==2:
            os.system('shutdown now')
        else:
            pass
        return redirect('/')
    except:
        return 'Failed'
    
@app.route('/reboot')
def reboot():
    try:
        p = getplatform()
        if p==1:
            os.system('shutdown -r -t 1')
        elif p==2:
            os.system('reboot')
        return redirect('/')
    except:
        return 'Failed'
    
    
@app.route('/cancle')
def cancle():
    try:
        p = getplatform()
        if p==1:
            os.system('shutdown -a')
        elif p==2:
            os.system('shutdown -c')
        return redirect('/')
    except:
        return 'Failed'
      
@app.route('/shutdownsettime/<t>')
def shutdownsettime(t):
    try:
        p = getplatform()
        if p==1:
            os.system('shutdown -s -t ' + str(int(t) * 60))
        elif p == 2:
            os.system('shutdown -h '+ t)
        return redirect('/')
    except:
        return 'Failed'
    
def getplatform():
    osName = platform.system()
    if(osName == 'Windows'):
        return 1
    elif(osName == 'Linux'):
        return 2
    elif(osName == 'Darwin'):
        return 3
    else:
        return 0
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9988', debug=True, threaded=True)