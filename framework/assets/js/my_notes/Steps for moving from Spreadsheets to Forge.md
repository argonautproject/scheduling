Steps for moving from spreadsheets to Forge
1. using last spreadsheet compatible build generate build to get the **definitions.xml** file
1. edit all the SD files to remove the following: ( create a transform )
   1. text element
   1. snapshot element
   1. existing mappings (since they are related to the base resource
1. Now ready to edit SD files in Forge
   - Recommend opening in Forge to sanitize some spreadsheet parsing errors
   - Simply open the files in Forge to edit
   - Save or Save As to local source folder : typically `source/resources`
      1. explore saving to Simplifier or GitHub repository directly
1. verify by running with the latest version of IG-Publisher.
