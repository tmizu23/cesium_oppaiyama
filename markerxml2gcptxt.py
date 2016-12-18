# encoding: utf-8
import xml.etree.ElementTree as ET


print("WGS84 UTM 54N")

tree = ET.parse('marker.xml')
root = tree.getroot()
camera={}
for child in root[0].findall('cameras')[0]:
    camera[child.attrib['id']]={'label':child.attrib['label']}

marker={}
for child in root[0].findall('markers')[0]:
   reference = child.find('reference')
   marker[child.attrib['id']]={'x':reference.attrib['x'],'y':reference.attrib['y'],'z':reference.attrib['z'],'enabled':reference.attrib['enabled']}


for child in root[0].findall('frames')[0]:
   for marker_id in child[0].findall('marker'):
       x = float(marker[marker_id.attrib['marker_id']]['x'])
       y = float(marker[marker_id.attrib['marker_id']]['y'])
       z = float(marker[marker_id.attrib['marker_id']]['z'])
       enabled = marker[marker_id.attrib['marker_id']]['enabled']
       for location in marker_id.findall('location'):
           img = camera[location.attrib['camera_id']]['label']
           pixcelx = float(location.attrib['x'])
           pixcely = float(location.attrib['y']) 
	   pinned = location.attrib['pinned']
           if enabled and pinned:
               print("{0:.1f} {1:.1f} {2:.0f} {3:.0f} {4:.0f} {5}".format(x,y,z,pixcelx,pixcely,img))

