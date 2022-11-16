from airium import Airium


class htmldoc:
    def __init__(self,name,title,body):
        self.title = title
        self.body=body
        self.name=name

    def CreateHtml():

        PageName=input("Name your Html file. No Spaces Allowed")
        f=open("%s.html"%PageName,'wb')
        return PageName


    def SetTitle(title):
        title=title
        topheadtag="<head>"
        bottomheadtag="</head>"
        SettingTitle=open("index.html",'w')
        #HtmlTitle = input("Desired title for your document")
        toptag=("<html>")
        bottomtag=("</html>")
        doctitle="<title>"+title+"</title>"

        SettingTitle.writelines(toptag) #top html tag
        SettingTitle.writelines(topheadtag)# top head tag
        SettingTitle.writelines(doctitle) #opening title tag
        SettingTitle.writelines(bottomheadtag) # closing title tag
        SettingTitle.writelines(bottomtag)   #bottom html tag

        SettingTitle.close()

    def SetTitleNotDefault(PageName,PageTitle):

        topheadtag = "<head>"
        bottomheadtag = "</head>"
        SettingTitle = open("%s.html"%PageName,'w')
        toptag = ("<html>")
        bottomtag = ("</html>")
        doctitle = "<title>" + PageTitle + "</title>"

        SettingTitle.writelines(toptag)  # top html tag
        SettingTitle.writelines(topheadtag)  # top head tag
        SettingTitle.writelines(doctitle)  # opening title tag
        SettingTitle.writelines(bottomheadtag)  # closing title tag
        SettingTitle.writelines(bottomtag)  # bottom html tag

        SettingTitle.close()

    def SetBody():
        OpeningBodyTag="<body>"
        ClosingBodyTag="</body>"

class Headings:

        def OpenLargestHeading():
            openingh1 = "<h1>"
            # SOP means Set On Page
            SOP_openingtag = open("index.html", 'w')
            SOP_openingtag.writelines(openingh1)
        def CloseLargestHeading():
            closingh1 = "</h1>"
            SOP_closingtag = open("index.html", 'w')
            SOP_closingtag.writelines(closingh1)

#used to be a main function at some point
#currentDoc=htmldoc.SetTitle()


class NavigationBar:
    def __init__(self,color,search_bar,icon_number,brand_name):
        self.color=color
        self.search_bar=search_bar
        self.icon_number=icon_number
        self.brand_name=brand_name

    def CreateNavbar(OnThisPage):
        color=input("What is the colour of your navigation bar?")
        havesearchbar=input("Do you want a search box for your navigation bar?")
        numberoficons=input("How many icons do you want on the navigation bar?")
        numberoficons=int(numberoficons)
        brand_name=input("What is your brand name? This will show on the Nav Bar")
        Link1Name =input("Enter name of link 1")
        Link2Name = input("Enter name of link 2")
        Link3Name = input("Enter name of link 3")
        Link4Name = input("Enter name of link 4")
        Link5Name = input("Enter name of link 5")
        Link6Name = input("Enter name of link 6")

        #opens current page and gets ready to insert the navbar to the page
        CreatingNavBar = open("%s.html"%OnThisPage,'w')

        #NavBar Attributes
        NavOpeningTagL="<nav"
        NavOpeningTagR=">"
        NavDarkBg="navbar navbar-expand-lg navbar-dark bg-dark"
        OpeningDivL="<div"
        ClosingDiv="</div>"
        RightAngleBracket=">"
        LeftAngleBracket="<"
        DivClassContainerFluid='class="container-fluid"'
        OpeningATagL="<a"
        ClosingATagR=">"
        ClosingATag="</a>"
        BrandName='class="navbar-brand" href="#"'
        TogglerButtor='button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"'
        OpeningITag="<i"
        ClosingITag="</i>"
        ClosingButtonTag="</button>"
        BarsIcon='class="fas fa-bars text-light"'
        CollapseNavBar='class="collapse navbar-collapse" id="navbarSupportedContent"'
        NavMeAuto='class="navbar-nav me-auto d-flex flex-row mt-3 mt-lg-0"'
        NavItemTextCenter='class="nav-item text-center mx-2 mx-lg-1"'
        FarEnvelope='class="far fa-envelope fa-lg mb-1"'
        NavLinkActive='class="nav-link active" aria-current="page" href="#!"' # put a variable in the #
        ListOpeningTag="<li"
        ListClosingTag="</li>"
        OpeningIconTagL="<i"
        OpeningIconTagR=">"
        ClosingIconTag="</i>"
        OpeningSpanTagL="<span"
        OpeningSpanTagR=">"
        ClosingSpanTag="</span>"
        RoundedPillBadgeNotificationWarning='class="badge rounded-pill badge-notification bg-warning"'
        NavDropdownText='class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDropdown"'
        OpeningULTagL="<ul"
        OpeningULTagR=">"
        ClosingULTag="</ul>"
        DropDownMenuDark='class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDropdown"'
        DropDownItem1='class="dropdown-item" href="#"'
        DropDownItem2='class="dropdown-item" href="#"'
        DropDownItem3='class="dropdown-item" href="#"'
        OpeningHrTag="<hr"
        ClosingHrTag="/>"
        DropDownDivider='class="dropdown-item" href="#"'

        #Configure the NavBar
        def setnavcolor(color):
            color=str(color).lower()




#A member of screen functions
def ScreenPrompt():
    ThisPageName=htmldoc.CreateHtml()
    #insert code to check if index.html already has a title
    DesiredTitle=input("What should be the title of your html document")
    htmldoc.SetTitleNotDefault(ThisPageName,DesiredTitle)
    NavBar=input("Do you need a navigation bar? (Y/N)")
    if NavBar.lower()=="y":



ScreenPrompt()

