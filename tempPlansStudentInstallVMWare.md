This is the instruction set for your students to download the necessary software to run the Virtual Machine (VM) on their Mac or Windows computers.

-----

# VM Setup: Host Machine Preparation

This guide will help you install the single piece of software needed on your personal computer (the "host machine") to run the course environment contained in the **OVA** file.

## Step 1: Download and Install VirtualBox

We will use **Oracle VM VirtualBox**, which is free and works identically on both Mac and Windows.

| Operating System | Download Link & Instructions |
| :--- | :--- |
| **Windows** | 1. Navigate to the official **VirtualBox website** download page. <br> 2. Click the link under **"Windows hosts"** to download the installer file (`.exe`). <br> 3. Run the installer and accept all the default settings. |
| **macOS** | 1. Navigate to the official **VirtualBox website** download page. <br> 2. Click the link under **"macOS hosts"** to download the disk image file (`.dmg`). <br> 3. Double-click the `.dmg` file and then double-click the **VirtualBox.pkg** file inside to start the installer. **Note:** On modern macOS, you may need to go to **System Settings $\rightarrow$ Security & Privacy** after the first failed attempt and click "Allow" next to the developer "Oracle America, Inc." |

-----

## Step 2: Download the Course VM Image

Download the compressed Virtual Machine image file (`.ova` extension) provided by your instructor.

  * **Download Link:** [Insert Your Hosting/Download Link Here]
  * **File Name:** `course-sandbox-v1.0.ova` (or similar)
  * **File Size:** [Insert File Size Here, e.g., \~5 GB]

**Important:** This is a very large file. Ensure you have a stable internet connection and enough free disk space.

-----

## Step 3: Import the VM Appliance

Once VirtualBox is installed and the `.ova` file is downloaded, you need to import the VM.

1.  **Open VirtualBox:** Launch the application.
2.  Go to the main menu and select **File $\rightarrow$ Import Appliance...** (or press $\text{Ctrl}+\text{I}$ / $\text{Cmd}+\text{I}$).
3.  Click the folder icon and navigate to where you saved the `.ova` file. Select it and click **Next**.
4.  Review the settings (you shouldn't need to change anything) and click **Import**.
5.  Read and accept the software license agreement.

VirtualBox will now take several minutes to copy and set up the VM. Once complete, the VM will appear in the list on the left side of the main VirtualBox window.

-----

## Step 4: Run the VM and Use Full Screen

### A. Initial Launch and Login

1.  Select the new VM in the list and click the **Start** button (the green arrow).
2.  After a short boot process, the Linux desktop will appear.
3.  **Login:**
      * **Username:** `student`
      * **Password:** `password123`

### B. Use Full Screen Mode

To ensure the best coding experience, you need the VM to take up your entire monitor. This is enabled by the installed **Guest Additions** software.

1.  Once you are logged into the VM, go to the top menu bar of the VirtualBox window.
2.  Select **View $\rightarrow$ Full-Screen Mode** (or press the keyboard shortcut $\text{Host}+\text{F}$).
      * **Host Key:**
          * **Windows:** The default Host Key is the **Right $\text{Ctrl}$** key.
          * **macOS:** The default Host Key is the **Left $\text{Command}$** key.
3.  Click **Switch** in the prompt that appears.

Your VM should now occupy your entire screen, functioning like a dedicated computer. To exit full screen, press the **Host Key + F** again.

**You are now ready to begin the Sandbox Setup Instructions (the next document) to install your tools and configure your terminal\!**
