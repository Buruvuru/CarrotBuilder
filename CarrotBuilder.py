#Finally Carrot Builder 1.0, A console application to build web pages

from setUp import SetProject

def CreateProject():
    selector=input("To Set Project Name, type 'setprojectname'")
    if selector.lower()=="setprojectname":
            PassedProjectCreation=SetProject.SetProjectNameAndLocation()
            #If  the project folder exists, PassedProjectCreation will be false and SetProject.SetProjectNameAndLocation
            #will run again

    if PassedProjectCreation==False:
        SetProject.SetProjectNameAndLocation()
    return PassedProjectCreation


CreateProject()
SetProject.CreateIndexFile()
