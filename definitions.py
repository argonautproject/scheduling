#! /usr/bin/env python3.

# create ig definition file with all value sets in the /resources directory
import json, os, sys, logging, re
from lxml import etree
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info('Start of program')
logging.info('The logging module is working.')
# create the ig.json file template as dictoinary


'''
ig_template = open(dir +'ig-template.json')  #ig-template  lack spreadsheet and valueset information
igjson = ig_template.read() # convert to strings
igpy =json.loads(igjson)  # convert to py dict format
'''

logging.info('create the ig.json file template as dictionary')

# globals

dir='/Users/ehaas/Documents/FHIR/Argo-Scheduling/'  # change to the local path name

''' this is the definitions file skeleton you need to modify as needed see ig publisher documenentation at  f http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. Note it includes the US-Core as a dependencyList'''

igpy = {"paths":{"temp":"temp","specification":"http://build.fhir.org","qa":"qa","txCache":"txCache","output":"output","pages":"pages","resources":["resources","examples"]},"extraTemplates":["mappings"],"defaults":{"StructureDefinition":{"template-base":"sd.html","template-defns":"sd-definitions.html","template-mappings":"sd-mappings.html"},"CapabilityStatement":{"template-base":"capst.html"},"CodeSystem":{"template-base":"codesys.html"},"ConceptMap":{"template-base":"cm.html"},"Any":{"template-format":"format.html","template-base":"base.html"},"ValueSet":{"template-base":"vs.html"},"OperationDefinition":{"template-base":"op.html"}},"source":"ig.xml","canonicalBase":"http://fhir.org/guides/argonaut-scheduling","tool":"jekyll","sct-edition":"http://snomed.info/sct/731000124108","dependencyList":[{"name":"uscore","location":"http://hl7.org/fhir/us/core/stu1/","source":"uscore"},{"name":"argopd","location":"http://www.fhir.org/guides/argonaut/pd/release1/","source":"argopd"}],"spreadsheets":[],"resources":{},"fixed-business-version" : "0.0.0", "version" : "3.0.1"}

logging.info('create the ig.xml file template as string')

''' this is the ig.xml file skeleton may need to modify as needed see ig publisher documenentation at  f http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. '''

igxml ='''<?xml version="1.0" encoding="UTF-8"?><!--Hidden IG for de facto IG publishing--><ImplementationGuide xmlns="http://hl7.org/fhir"><id value="ig"/><url value="http://fhir.org/guides/argonaut-scheduling/ImplementationGuide/ig"/><name value="Argo-Scheduling"/><status value="draft"/><experimental value="true"/><publisher value="Argonaut Project"/><package><name value="base"/></package><page><source value="index.html"/><title value="IG Templage Homepage"/><kind value="page"/></page></ImplementationGuide>'''

# ====================== this is all the same for all IGs ===================

# extension in spreadsheet - these need to be manually listed here needs to be named same as SD files

extensions = []

# operation in spreadsheet - these need to be manually listed here

operations = []

# search in spreadsheet - these need to be manually listed here

searches = []

#if valueset in spreadsheet is a codesystem - these need to be manually listed here

codesystems = []

#if valueset in spreadsheet is not a codesystem - these need to be manually listed

valuesets = []

#if structuremaps in spreadsheet is not a codesystem - these need to be manually listed

structuremaps = []


# =================Function definitions here=========================

def make_op_frag(frag_id):  # create [id].md file for new operations

    # default content for files
    op_frag = '''
    This is the  markdown file that gets inserted into the op.html template.
    '''
    # check if files already exist before writing files
    frag = dir + 'pages/_includes/' + frag_id

    fragf = open(frag + '.md', 'w')
    fragf.write(frag_id + '.md file\n' + op_frag)
    logging.info('added file: ' + frag + '.md')
    return

def make_frags(frag_id):  # create [id]-intro.md, [id]-search.md and [id]-summary.md files

    # default content for files
    intro = '''
    This is the introduction markdown file that gets inserted into the sd.html template.

    This profile sets minimum expectations for blah blah blah

    ##### Mandatory Data Elements and Terminology

    The following data-elements are mandatory (i.e data MUST be present). blah blah blah

    **must have:**

    1. blah
    1. blah
    1. blah

    **Additional Profile specific implementation guidance:**

    #### Examples
    '''
    srch = '''
    This is the search markdown file that gets inserted into the sd.html Quick Start section for explanation of the search requirements.
    '''
    sumry = '''
    This is the summary markdown file that gets inserted into the sd.html template. for a more formal narrative summary of constraints.  in future hope to automate this to computer generated code.

    #### Complete Summary of the Mandatory Requirements

    1.
    1.
    1.
    '''

    # check if files already exist before writing files
    frag = dir + 'pages/_includes/'+ frag_id

    fragf = open(frag + '-intro.md', 'w')
    fragf.write(frag_id + '-intro.md file\n' + intro)
    logging.info('added file: ' + frag + '-intro.md')
    fragf = open(frag + '-summary.md', 'w')
    fragf.write(frag_id + '-summary.md' + sumry)
    logging.info('added file: ' + frag + '-summary.md')
    fragf = open(frag + '-search.md', 'w')
    fragf.write(frag_id + '-search.md file\n' + srch)
    logging.info('added file: ' + frag +'-search.md')
    return



def update_sd(i,type,logical):
    namespaces = {'o': 'urn:schemas-microsoft-com:office:office',
                  'x': 'urn:schemas-microsoft-com:office:excel',
                  'ss': 'urn:schemas-microsoft-com:office:spreadsheet', }
    igpy['spreadsheets'].append(i)
    logging.info('adding ' + i + ' to spreadsheets array')
    sd_file = open(dir + 'resources/' + i)  # for each spreadsheet in /resources open value and read  SD id and create and append dict struct to definiions file
    sdxml = etree.parse(sd_file)  # lxml module to parse excel xml
    if logical:  # Get the id from the data element row2 column "element"
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[2]/ss:Cell[2]/ss:Data',namespaces=namespaces)  # use xpath to get the id from the spreadsheet and retain case
        temp_id = sdid[0].text # retain case
        update_igxml('StructureDefinition','logical' , temp_id)# add to ig.xml as an SD
    else:
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[11]/ss:Cell[2]/ss:Data',
                       namespaces=namespaces)  # use xpath to get the id from the spreadsheet and lower case
        temp_id = sdid[0].text.lower()  # use lower case
    update_igjson(type, temp_id) # add base to definitions file
    update_igjson(type, temp_id, 'defns') # add base to definitions file
    if not os.path.exists(dir + 'pages/_includes/'+ temp_id + '-intro.md'):  # if intro fragment is missing then create new page fragments for extension
        make_frags(temp_id)
    return

def update_igxml(type, purpose, id):
    ev = 'false'
    if purpose == "example":
        ev = 'true'
    vsxml = '<resource><example value="' + ev + '"/><sourceReference><reference value="' + type + '/' + id + '"/></sourceReference></resource>'  # concat id into appropriate string
    global igxml
    igxml = igxml.replace('name value="base"/>',
                            'name value="base"/>' + vsxml)  # add valueset base def to ig resource
    logging.info('adding ' + type + vsxml + ' to resources in ig.xml')
    return

def update_igjson(type, id, template = 'base', filename = "blah"): # add base to ig.json - can extend for other templates if needed with extra 'template' param
    if template == 'base':
        igpy['resources'][type + '/' + id] = {
            template : type + '-' + id + '.html'}  # concat id into appropriate strings and add valuset base def to resources in def file
        logging.info('adding ' + type + ' ' + id + ' base to resources ig.json')

    if template == 'source':
        igpy['resources'][type + '/' + id][template] =  filename  # concat filename + xml into appropriate strings and add source in def file
        logging.info('adding ' + id + ' source filename to resources ig.json')

    if template == 'defns':
        igpy['resources'][type + '/' + id][template] = type + '-' + id + '-definitions.html'  # concat id into appropriate strings and add sd defitions to in def file
        logging.info('adding ' + type + ' ' +  id  + ' definitions to resources ig.json')
    return


def update_def(filename, type, purpose):
      vsid_re = re.compile(r'<id value="(.*)"/>')  # regex for finding the index in vs
      vs_file = open(
            dir + 'resources/' + filename)  # can use a package like untangle or Xmltodict but I'm gonna regex it for now"
      vsxml = vs_file.read()  # convert to string
      vsmo = vsid_re.search(vsxml)  # get match object which contains id
      vsid = vsmo.group(1)  # get id as string
      update_igjson(type, vsid) # add base to definitions file
      update_igjson(type, vsid, 'source', filename) # add source filename to definitions file
      if type == 'StructureDefinition':
          update_igjson(type, vsid, 'defns')  # add base to definitions file
          if not os.path.exists(dir + 'pages/_includes/'+ vsid + '-intro.md'):  # if intro file fragment is missing then create new page fragments for extension
              make_frags(vsid)
      if type == 'OperationDefinition':
          if not os.path.exists(dir + 'pages/_includes/'+ vsid + '.md'):  # if file is missing then create new page fragments for extension
              make_op_frag(vsid)
      update_igxml(type, purpose, vsid)
      return

def update_example(type, id, filename):
      update_igxml(type, 'example', id)  # add example to ig.xml file
      update_igjson(type, id )  # add example base to definitions file
      update_igjson(type, id,'source', filename) # add source filename to definitions file
      igpy['defaults'][type] = {'template-base': 'ex.html'}  # add example template for type
      logging.info('adding example template to type ' +type + ' in ig.json')
      return


def get_file(e):
    ex_file = open(dir + 'examples/' + e)  # for each example in /examples open
    logging.info('load example xml file ' + dir + 'examples/' + e)
    return ex_file



def main():
    resources = os.listdir(dir + 'resources')  # get all the files in the resource directory
    for i in range(len(resources)):  # run through all the files looking for spreadsheets and valuesets
        if 'spreadsheet' in resources[i]: # for spreadsheets  append to the igpy[spreadsheet] array.
            if 'logical' in resources[i]:  # check if logical model
                logical = True #   these need to be handled differently
            else:
                logical = False
            update_sd(resources[i], 'StructureDefinition', logical) # append to the igpy[spreadsheet] array.
        if 'valueset' in resources[
            i]:  # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'ValueSet', 'terminology')
        if 'codesystem' in resources[
            i]:  # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'CodeSystem', 'terminology')
        if 'conceptmap' in resources[
            i]:  # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'ConceptMap', 'terminology')
        if 'capabilitystatement' in resources[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'CapabilityStatement', 'conformance')
        if 'operationdefinition' in resources[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'OperationDefinition', 'conformance')
        if 'structuredefinition' in resources[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'StructureDefinition', 'conformance')
        if 'searchparameter' in resources[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'SearchParameter', 'conformance')

   # add spreadsheet extensions
    for extension in extensions:
        update_igjson('StructureDefinition', extension, 'base')
        update_igjson('StructureDefinition', extension, 'defns')
        if not os.path.exists(dir + 'pages/_includes/'+ extension + '-intro.md'):  # if intro fragment is missing then create new page fragments for extension
            make_frags(extension)

    # add spreadsheet operations
    for operation in operations:
       update_igjson('OperationDefinition', operation, 'base')
    # add spreadsheet search parameters
    for search in searches:
       update_igjson('SearchParameter', search, 'base')
    # add spreadsheet code systems
    for codesystem in codesystems:
       update_igjson('CodeSystem', codesystem, 'base')
       update_igjson('ValueSet', codesystem, 'base')
    # add spreadsheet valuesets
    for valueset in valuesets:
       update_igjson('ValueSet', valueset, 'base')
    # add spreadsheet structuremaps
    for structuremap in structuremaps:
       update_igjson('StructureMap', structuremap, 'base')

    examples = os.listdir(
        dir + 'examples')  # get all the examples in the examples directory assuming are in json or xml
    for i in range(len(examples)):  # run through all the examples and get id and resource type
        if 'json' in examples[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            exjson = json.load(get_file(examples[i]))
            extype = exjson['resourceType']
            ex_id = exjson['id']
            update_example(extype, ex_id, examples[i])
        if 'xml' in examples[
            i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            ex_xml = etree.parse(get_file(examples[i]))  # lxml module to parse example xml
            ex_id = ex_xml.xpath('//f:id/@value', namespaces={'f': 'http://hl7.org/fhir'})  # use xpath to get the id
            extype = ex_xml.xpath('name(/*)')  # use xpath to get the type '''
            update_example(extype, ex_id[0], examples[i])

    # write files
    ig_file = open(dir + 'ig.json', 'w')
    ig_file.write(json.dumps(igpy))  # convert dict to json and replace ig.json with this file
    logging.info('ig.json now looks like : ' + json.dumps(igpy))

    ig_file = open(dir + 'resources/ig.xml', 'w')
    ig_file.write(igxml)  # replace ig.xml with this file
    logging.info('ig.xml now looks like : ' + igxml)
    return


#main

if __name__ == '__main__':
    main()
    logging.info('End of program')
