# Background
My car doesn't support reading genre metadata from files off of a flash drive.
To maintain the ability to play genres from a flash drive I am using an automatically
generated directory system instead from a quick hacky script.

 # What does the script do?
 It reads through the file system starting at the given root directory in setting's line 1
 and copies files that match the directory provided in setting's line 3 into a flattened
 version in a new directory directly under the provided root directory. It also copies any
 potential genres into their own flattened directories.
 
 # Expected File System
  - \<root from setting's line 1\>
    - \<music type A\>
        - \<music series A\>
            - \<directory which includes setting's line 3 to indicate music should be copied\>
                - \<genre A where A exists in setting's line 4\>
                    - \<files in genre A to be copied and flattened\>
                - \<files to be copied and flattened\>
            - \<any files that you don't want copied\>
        - \<music series B\>
        - ...
    - \<music type B\>
    - ...
 
 # Settings
 Settings are specified in [settings.txt](./settings.txt)
 - Line 1: the root directory to read from
 - Line 2: the suffix to apply to flattened directories
 - Line 3: the required string to match for copying a directory
 - Line 4: comma delimeted genres
  