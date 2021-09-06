import clr
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V16\\PublicAPI\\V16\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
# import Siemens.Engineering.HW.Features as hwf
# import Siemens.Engineering.Compiler as comp
from datetime import datetime

processes = tia.TiaPortal.GetProcesses() # Making a list of all running processes
mytia = processes[0].Attach()
tiaProject = mytia.Projects[0]
timeString = datetime.now().strftime('%Y%m%d_%H%M')

folderPath = "D:\\Archive\\"
directoryPath = DirectoryInfo(folderPath)

tiaProject.Archive(directoryPath, tiaProject.Name + "_" + timeString + ".zap16", 1)

