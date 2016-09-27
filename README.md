# AVON
A badass sequencer named AVON

How to sync your local changes to GitHub.

1. Edit some file in your local copy C:\Users\Hallgrimur\AVON.  Save the file.
2. Open Git GUI in your start menu.
3. Under "Open Recent Repository" click ~/AVON.
4. Click "Rescan", then "Stage Changed."
5. Under "Commit Message" write something witty, then click "Commit."
6. Click "Push," then in the dialog box, leave all the settings as they are, and click the "Push" button.
7. Provide your Git username/password when prompted to do so.

Now your changes are saved to GitHub!



How to sync your local files to the newest versions on GitHub (how to download other peoples' changes).  Easier if you use BASH, but you can use GUI to do the same thing.


1. Open Git GUI in your start menu.
3. Under "Open Recent Repository" click ~/AVON.
3. Remote > Fetch from > upstream, close dialog box.
4. Branch > Checkout, leave settings alone and click Checkout button.
5. Merge > Local merge, after "Revision Expression" type "upstream/master" and click Merge button.

OR

1. Open Git BASH.
2. cd AVON
3. git fetch upstream
4. git checkout master
5. git merge upstream/master

Done!