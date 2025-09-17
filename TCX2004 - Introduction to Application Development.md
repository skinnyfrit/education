# Course Outcomes
**Aims & Objectives**

**Syllabus**
Basics of application development and software engineering (technologies, approaches, principles and issues in designing IT applications systems)  
Major topics:
- rapid web frameworks
- scripting languages
- web and mobile interfaces
- designing and deploying web and mobile services
- operational considerations
- technical tradeoffs
Tools and techniques for app dev: 
- object-oriented system modelling
- testing methodologies
- security techniques

**Learning Outcomes**
1. Develop an appreciation for the technologies available, and develop expertise in the current technologies, as they are used in application systems development.
2. Develop the technical and conceptual capabilities to design and deploy applications within and across Internet, web, and mobile platforms.
3. Understand state-of-the-art application development techniques, such as object-oriented system modelling and design.
4. Be aware of common security risks when developing applications and ways to prevent them.

## Table of contents  

0. [Setup](#l01-setup)
1. [Project Management](#l02-project-management)
3. [Requirements](#l03-requirements)
4. [Object-Oriented Design](#l04-object-oriented-design)
5. [Backend - FastAPI](#l05-backend---fastapi)
7. [Deployment](#l07-deployment)
8. [Frontend - Javascript](#l08-frontend---javascript)
9. [Integration](#l09-integration)
10. [Frontend - HTML + CSS](#l10-frontend---html--css)
11. [Frontend - React Native](#l11-frontend---react-native)
12. [Security](#l12-security)
13. [Summary](#l13-summary)

# L01: Setup
## 1.1 *nix Command Line Interface (CLI)
### Command prompts
|  | Terminal (emulated)/Console (physical) | Shell | Linux Command Prompt |
|---|---|---|---|
| What it is | keyboard inputs -> prints text output to user | interacts w OS to execute commands (from terminal or scripts) | user ($, %) or root (#) types a command for shell to execute task |
| Examples | WIN Terminal, Linux Terminal, mac xterm/Console/konsole | WIN powershell MS-DOS, Linux Bourne Shell, Bourne Again Shell, Mac Z shell | [user_1@personalcomputer:-]$ |

### Control Sequences (Shortcuts/Hotkeys)  
- `Ctrl` + `d` : Exit/end of input to a program
- `Ctrl` + `c` : Terminate current program
- `Ctrl` + `z` : Suspend current program
    - `fg` suspended program brought to foreground
    - `bg` suspended program brought to background
> [!IMPORTANT]
> Do not use Suspend `Ctrl` + `z`  to Terminate `Ctrl` + `c` !

### Command Documentation
- `man` MANual : interactive manual for `ls`. ( quit using `q` )
- `info` INFOrmation : alternative to `man` but not widely used
- `help` or `-h` or `--help` Help command : find help about commands

## 1.2 Linux Navigation
**Windows vs *nix system**
|  | Windows | *nix |
|---|---|---|
| Organization | Usually C:\ | Single 'root' / |
| Case | insensitive | sensitive |
| Path separator | \ | / |
| Forbidden char | `<>:"/\|?*` | `/` |
| File system | NTFS, exFAT | UFS(Unix), Ext4(Linux), APFS(MacOS) |
| Hidden files | File Property | Names starting with `.` |

***nix Pathing**
`~` home directory  
`.` current working directory (cwd)  
`..` parent directory (prev dir)  
`pwd` prints working directory  
`ls` LiSts contents of a directory  
`mkdir` MaKe a subDIRectory  

## 1.3 Linux File Management
`cd` Change Directory  
`rmdir` ReMove a subDIRectory  
`cp` CoPy subdirectory/file  
`mv` MoVe subdirectory/file  
`rm` ReMove subdirectory/file  
`cat` CATenate file to screen  

> [!NOTE]
> `ls` and `cat` are different!

## 1.4 Connect to Remote Server
**SSH (Secure Shell Protocol)**  
`ssh <username>@<hostname>`
- <username> is remote username
- <hostname> is address or hostname of remote computer (server/host)

**Copy to/from local/remote**  
`scp <source> <destination>`
- local: <path> (same as `cp`)
- remote: <username>@<hostname>:<path>

# L02: Project Management
## 2.1 Revision Control
Revision Control Software (RCS) allows for tracking, collaboration, recovery and parallel work.  
### Git
Fun fact: Git was created by creator of Linux!  
**Git Hosting Platforms**
- GitHub
- GitLab
- Bitbucket
- Azure Repos
- SourceForge

Typical Git Workflow:  
- Initialize: Config -> Create -> Clone -> Fork
- Saving History: Stage -> Comment -> Push -> Merge
- Using History: Tag -> Diff -> Checkout -> Pull

### Setting up & CLI git commands
**Config**  
> `git config --global user.name "Your Name"`
> `git config --global user.email "email@email.com"`
- `global` sets these values for ALL repo on local machine

**Create**  
> `git init`
- creates new empty repo (.git folder) in cwd

**Clone**  
> `git clone <repo-url>`
- Cloning also downloads entire revision history

**Fork**  
> `gh repo fork <repo-url>`
- Creates a remote copy of a remote repo (`upstream`)
- Allows experimentation of repo you don't control
- Propose changes back via a pull request (mechanism for contributing code to remote repo)

**Stage**  
> `git add <file>`
- Mark changes in working directory to include next commit

**Commit**  
> `git commit -m "message"`
- Save staged changes as a new revision in the history

**Push**  
> `git push`
- Copy your latest commits from your local repository to a remote repository.
> [!IMPORTANT]
> Pushing is only possible if both repos share common history

**Merge**  
> `git merge <branch>`
- Combine changes from diff branches/sources into current branch
- Resolve conflicts, complete merge with `git add <file>`

**Pull**
> `git pull`
- Fetch & integrate changes from remote repo to current branch
- Combines fetch (download changes) and merge (integrate changes)

**Diff**
> `git diff <branch1> <branch2>`
- Shows difference between files/commits/branches OR unstaged changes in working directory (if used without branches)

**Checkout**
> `git checkout <branch>`
- Switches to specific branch
- Restore file to previous state: `git checkout <commit> -- <file>`

**Tag**
> `git tag <tagnanme>` (or `git tag` to list all tags)
- Mark specific points in history as important (e.g. releases)
- Annotated tag (with optional message): git tag -a <tagname> -m "message"

## 2.2 Project Planning
### Team Structures
- Egoless
    - All members share equal responsibility & make decisions by consensus
- Chief programmer
    - Single chief programmer takes lead and makes key decisions
- Strict hierarchy
    - Clear chain of command w/ each member reporting to a superior

### Work Breakdown Structure
| Task ID | High Level Task | Estimated Effort | Pre-req Task |
|---|---|---|---|
| A | Major Task 1 | 1 man day | - |
| B | Major Task 2 | 1.5 man days | A |
| C | Major Task 3 | 2.5 man days | A |

Task Breakdown  
| Task ID | Task | Estimated Effort | Pre-req Task |
|---|---|---|---|
| C.1 | Well-defined task (when task is considered done) | 1 man day | A |

### Milestones
End of a stage indicating significant progress.
- Intermediate product release
- Should account for dependencies and priorities

Example:  
| Iteration | Description |
|---|---|
| 1 | Backend Prototype |
| 2 | Website Prototype |
| 3 | Mobile Prototype |

### Issue Trackers (bug trackers)
Check GitHub Issues tab

### Gantt Charts
Time vs Tasks (represented using horizontal bars)

### PERT Charts
Program Evaluation Review Technique (PERT) chart shows order/sequence of tasks

## 2.3 SDLC Process Models
Software Development Life Cycle (SDLC):
1. Requirement
2. Analysis
3. Design
4. Implementation
5. Testing

### Process Models
1. Sequential model (Waterfall)
    - linear process
2. Iterative model (unified process)
    - Each iteration builds on previous versions, gradual improvements
    - breadth-first: updates most components and features parallel (working product each time)
    - depth-first: develops some components in detail (may not always be working, esp at the start)
    - Unified Process: Flexible and customizable process model framework rather than a single fixed process.
        - Phases|Activities|Typical Artifacts
3. Agile model *(considered iterative)* (e.g. Scrum, Extreme Programming (XP))
    - Emphasise flexibility + collaboration + rapid delivery of small, functional increments
    - Agile manifesto
    - Scrum vs Extreme Programming

# L03: Requirements

# L04: Object-Oriented Design

# L05: Backend - FastAPI

# L06: Advanced - FastAPI

# L07: Deployment

# L08: Frontend - Javascript

# L09: Integration

# L10: Frontend - HTML + CSS

# L11: Frontend - React Native

# L12: Security

# L13: Summary