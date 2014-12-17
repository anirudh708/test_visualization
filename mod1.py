'''
Created on Dec 15, 2014

@author: Anirudh
'''

# import pysvg
# import svgwrite
# import matplotlib.pyplot as py
# import numpy as np
from  tornado.web import *
import os
#from tornado.web import Application
# from io import StringIO
# from locale import format
#import tornado
# import pdfkit


# py.bar([0,1,2,3,4,5,6,7,8,9], [23,80,92,62,98,7,9,56,19,68], width=0.8, bottom=None, hold=None)
# 
# py.show()
# 
# py.savefig("E:\\signal", ext="svg", close=True, verbose=True)

# x=np.array([1,2,3])
# y=np.array([1,1,3])
# 
# z= np.square(x)*2000
# 
# py.scatter(x, y, s=z)
# py.show()

# R=np.corrcoef([[1,2,3],[2,4,6],[-1,-2,-3]])
# print R.T
# py.pcolor(R)
# py.colorbar()
# py.yticks(np.arange(0.5,2),range(1,3))
# py.xticks(np.arange(0.5,2),range(0,2))
# py.show()

class MainHandler(RequestHandler):
    def get(self):
        self.write('hello sneha paturu')

class ImageHandler(RequestHandler):

    def get(self):
#         d={}
#         d["mov1"]=1
#         d["mov2"]=10
#         d["mov3"]=40
#         d["mov4"]=3
#         py.bar(range(len(d)),d.values(),align="center")
#         py.xticks(range(len(d)),d.keys())
#         io=StringIO()
#         py.savefig(io,format='svg')
#         self.set_header("Content-Type", "image/svg+xml")
#         print io.getvalue()
#     
#         config = pdfkit.configuration(wkhtmltopdf='E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
#         
#         pdfkit.from_string(io.getvalue(),"E:\\hello.pdf",configuration=config)
#     
#         self.write(io.getvalue())
        self.write("chunk")
        

app = Application([
    url(r"/", MainHandler),
    #url(r"/Image",ImageHandler)
    ])

if __name__=="__main__":
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
    





