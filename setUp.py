import os

class SetProject:
    def __init__(self,ProjectNameAndLocation,IncludeBootstrap,UseIndex):
        self.SetProjectNameAndLocation=ProjectNameAndLocation
        self.IncludeBootstrap=IncludeBootstrap
        self.UseIndex=UseIndex

    def SetProjectNameAndLocation():

        FunctionSuccessChecker=True
        ProjectName=input("Name your project")
        print("Automatic configuration / auto")
        print("Custom Path / cstpath")
        ConfigurationChoice=input()
        if ConfigurationChoice.lower()=="auto":
            #directory=ProjectName
            NewPath="C:/CarrotBuilder/%s."%ProjectName
            if not os.path.exists(NewPath):
                os.makedirs(NewPath)
            else :
                print("Path Exists")
                #FunctionSuccessChecker is a boolean variable
                FunctionSuccessChecker=False
        return FunctionSuccessChecker

    def CreateIndexFile():

        open("index.html",'w')




