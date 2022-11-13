# from kivy.app import App
# from plyer import gps

# class GpsTest(App):
#     def on_start(self):
#         gps.configure(onlocation=self.on_gps_location)
#         gps.start()

#     def on_gps_location(self, **kwargs):
#         kwargs['lat'] = 10
#         kwargs['lon'] = 10
#         print(kwargs)

# GpsTest.run()

######################################################
# from plyer import gps


# def storeLocation(**kwargs):
#     locationData = kwargs
#     return locationData


# def getLocation():
#     gps.configure(on_location=storeLocation)
#     gps.start(minTime=1000, minDistance=1)
#     gps.stop()
#####################################################

from kivy.app import App 
from kivy.uix.label import Label 
from plyer import gps

class ClientLocation(App): 
    def on_start(self): 
        gps.configure(on_location=self.on_location) 
        self.on_resume() # I still don't know what the mainthread decorator does

    def on_location(self, **kwargs):
        # The kwargs should be sent to the server, but will be printed to the console for now
        print(kwargs)

    # Can you explain what on_status() does, or should do?

    def on_resume(self):
        gps.start()

    def on_stop(self):
        self.on_pause()

    def on_pause(self):
        gps.stop()
        
    def build(self):
        return Label(text="GPS WORKING!")
    
ClientLocation().run()