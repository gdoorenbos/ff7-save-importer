# ff7-save-importer
Final Fantasy VII Save Importer - imports FF7 saves from the Android port to PC, updating the metadata file that the save file is validated against.  

## Instructions:
* Clone or download this repository in Windows.
* Copy the save file from Android (save00.ff7) into the repository folder in Windows.
  * This can be accomplished in a variety of ways. I use my google drive, but you could also use a bluetooth transfer, USB transfer, or whatever floats your boat.
* Run ff7_update_save.py, either from the command line or by double-clicking it in the file explorer.

## Copying back to Android
The Android port doesn't have a metadata file that the save file is validated against. simply copy the save00.ff7 file from your PC to your Android device.

## Paths
**Android path:** Android/data/com.square_enix.android_googleplay.FFVII/files/Documents/save00.ff7  
**PC path:** %USERPROFILE%\Documents\Square Enix\FINAL FANTASY VII Steam\user_<user_id>\save00.ff7  
