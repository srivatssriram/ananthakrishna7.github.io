with open("homepage-ass.html", "a") as file:
    l = ["19MAT112 - Linear Algebra", "19PHY101 - Engineering Physics - A", "19CSE102 - Computer Programming", "19EEE111 - Electrical and Electronics Engineering", "19EEE182 - Electrical and Electronics Engg Practice", "19CSE103 - User Interface Design", "19CSE111 - Fundamentals of Data Structures", "19MEE181 - Manufacturing Practice", "22ADM111 - Cultural Education - II"]
    for i in l:
        file.write(f"\n\t\t<div class='assignments' id='{i[0:8:1]}'>\n\t\t\t<h3>{i}</h3>\n\t\t\t<ol>\n\t\t\t\t<li></li>\n\t\t\t\t<li></li>\n\t\t\t\t<li></li>\n\t\t\t</ol>\n\t\t</div>")

