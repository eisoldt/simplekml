import os
import glob
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import simplekml

formatter = HtmlFormatter(linenos=True, noclasses=True)
formatter.get_style_defs('.highlight')

file_path, file_name = os.path.split(os.path.abspath(__file__))

folders = ['examples', 'tutorials']

kml = simplekml.Kml()
kml.document = simplekml.Folder(name="Samples Index")
kml.document.open = 1

for folder in folders:
    folder_path = os.path.join(file_path, folder)
    kml_folder = kml.newfolder(name=folder)
    kml_folder.liststyle.listitemtype = simplekml.ListItemType.checkoffonly

    for py in glob.glob(folder_path + '/*.py'):
        if os.path.split(py)[1] != file_name:
            name = os.path.splitext(os.path.split(py)[1])[0]
            netlink = kml_folder.newnetworklink(name=name)
            netlink.description = ""
            netlink.snippet.maxlines = 1
            netlink.visibility = 0
            lines = ""
            with open(py, 'r') as py_file:
                comment = 0
                heading = ""
                for line in py_file:
                    if comment < 2:
                        if line.strip() == '"""':
                            comment += 1
                        heading += line.strip().strip('"')
                        if comment == 2:
                            netlink.snippet.content = heading
                            netlink.description += '<i>{0}</i></br></br>'.format(heading)
                    else:
                        lines += line
            html = highlight(lines, PythonLexer(), formatter)
            netlink.description += html
            netlink.link.href = "https://raw.githubusercontent.com/eisoldt/simplekml/master/samples/{1}/{0}.kml".format(name.replace(" ", "%20"), folder.lower())

kml.save(os.path.splitext(__file__)[0] + ".kml")



