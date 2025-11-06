This is a fantastic approach. Giving students a sandboxed environment where they learn to install tools *and* configure their own productive shell is a powerful lesson.

Here is the markdown instruction set for your students, with a strong opinionated setup for the terminal, focusing on a robust, feature-rich experience.

-----

# Course VM: Sandbox Setup Instructions

Welcome to your consistent, cross-platform learning environment\! This Virtual Machine (VM) runs a lightweight Linux distribution (**Manjaro XFCE**). Your first assignment is to set up your personal developer toolkit inside this sandbox.

If you ever break the VM, just delete it and re-import the original **OVA** file to start fresh\!

-----

## Step 1: Initial Login and Security

1.  **Login:** Start the VM and log in using the universal credentials:

      * **Username:** `student`
      * **Password:** `password123`

2.  **Change Your Password:** You have administrative (admin) rights in this VM. To protect your work, immediately change your password.

    ```bash
    passwd
    ```

    *Enter the current password (`password123`), then your new password twice.*

-----

## Step 2: The Command Line: Zsh and Oh My Zsh

The terminal is your primary tool. We're upgrading from the basic shell to **Zsh** and installing the **Oh My Zsh** framework for better themes, history, and user experience.

### A. Install Zsh and Git

We'll use Manjaro's package manager (`pacman`) for this.

```bash
# Update the system first
sudo pacman -Syu

# Install zsh and git
sudo pacman -S zsh git
```

### B. Install and Configure Oh My Zsh

Oh My Zsh is a community-driven framework for managing your Zsh configuration. It gives you access to themes, plugins, and enhanced history features.

1.  **Install Oh My Zsh:** Use the command below to download and run the installer script.

    ```bash
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

    *The script will ask if you want to switch your default shell to Zsh. **Type `Y` and hit Enter**.*

2.  **Install Powerline Fonts (for Themes):** Many modern themes use special characters (like arrows and glyphs) that require a compatible font to display properly (this enables your **unicode** features\!).

    ```bash
    sudo pacman -S powerline-fonts
    ```

3.  **Choose a Theme:** Open the Zsh configuration file using a terminal editor:

    ```bash
    nano ~/.zshrc
    ```

    *Find the line starting with `ZSH_THEME="..."` and change the theme name. Popular choices for a clean, professional look are `agnoster`, `clean`, or `powerlevel10k` (which requires its own separate setup, but is excellent).*

      * **Suggestion:** Try `ZSH_THEME="agnoster"` or `ZSH_THEME="clean"`.

4.  **Enable Better History:** Add the following lines to the end of the `~/.zshrc` file to ensure history is saved robustly, even across multiple windows, and can be scrolled back extensively.

    ```bash
    # Set history file size and save settings
    HISTSIZE=100000
    SAVEHIST=100000
    setopt appendhistory
    setopt inc_append_history
    ```

5.  **Apply Changes:** Close and reopen your terminal to activate Zsh and your new theme.

-----

## Step 3: Core Toolchain Installation

Now that your command line is ready, install the required development languages and tools.

### A. R and Python

Install the core languages using `pacman`:

```bash
sudo pacman -S r python python-pip
```

### B. uv (Python Package Installer)

We'll install `uv` by downloading the official binary and adding it to your system's search path (`$PATH`). This is a common way to install modern tools.

1.  **Run the Installer:**

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Note the PATH:** The installer will tell you where it placed the `uv` binary (usually `~/.cargo/bin`). **Take note of this path.**

3.  **Update Zsh PATH:** Open your `~/.zshrc` file again and add a line to ensure `uv` can be run from anywhere. **Change the path below to match the path the installer gave you\!**

    ```bash
    nano ~/.zshrc
    # Add this line near the end (adjust the directory if necessary)
    export PATH="$HOME/.cargo/bin:$PATH"
    ```

4.  **Apply Changes:** Source the file or restart your terminal:

    ```bash
    source ~/.zshrc
    # Test it:
    uv --version
    ```

### C. Quarto

Quarto is a separate package. We will install it directly using the official Manjaro/Arch method for simplicity.

```bash
# Install Quarto (it might be in the community repo or AUR on Manjaro)
pamac install quarto
```

*Note: If `pamac` asks you to confirm dependencies, type `Y` and Enter.*

### D. Emacs and VS Code

Install both text editors/IDEs:

```bash
# Install Emacs and VS Code (the 'code' package)
sudo pacman -S emacs code
```

-----

## Step 4: Configure VS Code (The IDE)

1.  Launch **VS Code** from the application menu.

2.  **Install Extensions:** Use the Extensions view (Ctrl+Shift+X or ⌘+Shift+X) to search for and install the following extensions.

      * **Quarto:** For writing and rendering documents.
      * **R:** For R language support.
      * **Python:** For Python language support.

3.  **Test:** Create a new Python file (`test.py`) or Quarto document (`test.qmd`) and ensure the syntax highlighting and language features are active. You're ready to code\!
