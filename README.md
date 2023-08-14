# Awesome Structure Editors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A list of structural/projectional code editor projects.

Any comments, suggestions? [Let us know!](https://github.com/yairchu/awesome-structure-editors/issues)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Contents

- [Foreword](#foreword)
- [Structural code editor projects](#structural-code-editor-projects)
  - [Unreleased Projects](#unreleased-projects)
  - [Concluded or inactive projects](#concluded-or-inactive-projects)
- [Blocks Programming Editors](#blocks-programming-editors)
- [Spreadsheet-based projects](#spreadsheet-based-projects)
- [Other notable projects](#other-notable-projects)
- [Resources](#resources)
  - [Related lists](#related-lists)
  - [Community](#community)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Foreword

Projectional editing is how almost all document editing applications work nowadays, except for editing source code and text documents, where it is still common to edit plain text files that are parsed to render/compile the result.

This document is a list of projects trying to bring the projectional/structural approach to source code editing.

As evident from the wealth of ongoing and concluded attempts listed below, this problem appears to be either difficult, or impossible. Hopefully one or more of these projects will succeed in realising it and bringing it to the mainstream!

## Structural code editor projects

This list includes projects which are actively developed or were maintained recently. Currently the bar for incomplete projects is set arbitrarily at 2020.

Project properties are summarized using unicode/emoji "flags":
- Project structure: 💵 Commercial, 🎓 Academic, ♡ Accepts donations
- UX: 📖 Uses text files, ⤴️ Visual programming, ⌨️ Text editing like UX
- Target languages: 👶 New language, λ Functional, ｟ Lisp-based, ☕ JavaScript/TypeScript, 🧰 Language Workbench
- Other: 🔨 Is in some production use, 🌐 Works in browser, 👨‍👩‍👧‍👦 Not intended for programmers, 文 Localization support

| Project | Properties | Description | Written in | ⭐️ | Updated
|--------:|:----------:|:------------|:----------:|:--:|:-------:
| [Enso](https://enso.org) | 💵 📖 ⤴️ 👶 λ | Hybrid visual+textual programming language | Scala, Rust | [6571](https://github.com/enso-org/enso) | 2023
| [Unison](https://unisonweb.org) | 💵 📖 👶 λ | Code database projected to text-files edited in your text editor of choice. Originally centered around having a projectional editor, but pivoted to creating a cloud programming language first | Haskell | [5301](https://github.com/unisonweb/unison) | 2023
| [Lamdu](http://www.lamdu.org) | ♡ ⌨️ 👶 λ 文 | Language with live programming and novel UX for type errors | Haskell | [1831](https://github.com/lamdu/lamdu) | 2023
| [MPS](https://www.jetbrains.com/mps/) | 💵 ⌨️ 🧰 🔨 | Language workbench for projectional languages | Java | [1452](https://github.com/JetBrains/MPS) | 2023
| [Dark](https://darklang.com) | 💵 ⌨️ 👶 λ 🌐 | Platform and language as a service for app backends and web | F#, ReScript | [1392](https://github.com/darklang/dark) | 2023
| [Cursorless](https://www.cursorless.org/) | ♡ 📖 🔨 | Spoken language for structural code editing | TypeScript | [637](https://github.com/cursorless-dev/cursorless) | 2023
| [Hazel](http://hazel.org) | 🎓 ⌨️ 👶 λ 🌐 | Language with live programming and typed holes | Reason | [603](https://github.com/hazelgrove/hazel) | 2023
| [JOY.js](https://ncase.me/joy/) | ♡ 👶 🧰 🔨 🌐 👨‍👩‍👧‍👦 | Language workbench for programmable demos | JavaScript | [555](https://github.com/ncase/joy) | 2018
| [Fructure](https://fructure-editor.tumblr.com) | ｟ 🧰 | A projectional editor workbench for Racket-implemented languages | Racket | [412](https://github.com/disconcision/fructure) | 2020
| [Sapling](https://github.com/kneasle/sapling) | ⌨️ | Vim/Kakoune-inspired modal structured editor for existing languages | Rust | 393 | 2023
| [tylr](https://tylr.fun) | 🎓 ⌨️ λ 🌐 | A tiny tile-based editor for well-formedly manipulating sequences of tokens | Reason | [249](https://github.com/hazelgrove/tylr) | 2022
| [Cirru](http://cirru.org) | ｟ | A tree editor for ClojureScript | Clojure | [212](https://github.com/Cirru/calcit-editor) | 2023
| [Holbert](http://liamoc.net/holbert) | 🎓 🌐 | A graphical interactive proof assistant designed for education | Haskell | [154](https://github.com/liamoc/holbert) | 2023
| [ProjecturEd](https://github.com/projectured/projectured) | 👨‍👩‍👧‍👦 | General purpose projectional editor | Common Lisp | 131 | 2022
| [Vlojure](https://vlojure.io) | ⤴️ ｟ 🌐 | A novel visual UX for ClojureScript | Clojure | [130](https://github.com/Ella-Hoeppner/Vlojure) | 2022
| [Tofu](https://github.com/Gregoor/tofu) | ♡ ☕ | VSCode extension for structured editing of JavaScript and TypeScript | TypeScript | 93 | 2022
| [Envision](http://dimitar-asenov.github.io/Envision/) | 🎓 👶 | Editor for a Java/C++ like language | C++ | [92](https://github.com/dimitar-asenov/Envision) | 2022
| [Subtext](http://www.subtext-lang.org) | 👶 | A series of inspiring presentations and projects exploring ideas in projectional editing | TypeScript | [92](https://github.com/JonathanMEdwards/subtext10) | 2022
| [Eyg](https://eyg.run) | 👶 λ 🌐 | Minimal language to enable exploration of alternative editing methods | Gleam | [64](https://github.com/crowdhailer/eyg-lang) | 2023
| [Freon](https://www.projectit.org) | ⌨️ 🧰 🌐 | Web-based Projectional Language Workbench | TypeScript | [57](https://github.com/projectit-org/ProjectIt) | 2023
| [Forest](https://github.com/tehwalris/forest) | ☕ 🌐 | A prototype tree editor for TypeScript | TypeScript | 52 | 2023
| [Lisperanto](https://github.com/uprun/lisperanto) | ♡ ｟ 🌐 | IDE for Lisp-like language | JavaScript | 39 | 2022
| [Foundry](https://github.com/int-index/foundry) | λ | A projectional editor for the Morte language | Haskell | 28 | 2022
| [Gopcaml-mode](https://gitlab.com/gopiandcode/gopcaml-mode) | 📖 λ 🔨 | Structural editing Emacs plugin for OCaml code | OCaml | [19](https://github.com/gopiandcode/gopcaml-mode) | 2022
| [Frugel](https://github.com/cdfa/frugel) | 🎓 ⌨️ 👶 λ | A research exploring a novel UX for textual entry of code | Haskell | 17 | 2022
| [SplootCode](https://splootcode.io) | ⌨️ 🌐 | A structural editor for Python, aimed towards beginners | ? | - | 2023
| [Alfa](https://cth.altocumulus.org/~hallgren/Alfa/index.html) | 🎓 λ | An editor for Agda which doesn't allow incorrect code | Haskell | - | 2020
| [OCell](http://kevinmahoney.co.uk/ocell/) | 👶 🌐 | ? | ? | - | 2020

### Unreleased Projects

| Project | Properties | Description
|--------:|:----------:|:------------
| [Roc](https://www.roc-lang.org) | λ | A performance oriented functional programming language [with a structural editor](https://youtu.be/ZnYa99QoznE?t=5864).
| [Dion Systems](https://dion.systems) | |
| [Neurion](https://neurion.co) | 💵 👶 λ |

### Concluded or inactive projects

| Project | Time_Period | Properties | Description
|--------:|:------:|:----------:|:------------
| [Inflex](https://chrisdone.com/posts/inflex/) | 2020 - 2022 | 💵 🌐 👶 λ | A spreadsheet-inspired functional programming language
| [Intentional software](https://en.wikipedia.org/wiki/Intentional_Software) | 1990s - 2017 | 💵 | Started as a Microsoft project to develop a projectional editor in the late 1990s (see [video from 2000](https://youtu.be/tSnnfUj1XCQ)), which later spun up as an independent company, which later pivoted to develop a language workbench. Despite being founded and self-funded by [a Billionaire](https://en.wikipedia.org/wiki/Charles_Simonyi), it was ultimately acquired by Microsoft at 2017, with the original projects being cancelled (afaik).
| [Eve](https://futureofcoding.org/essays/eve/) | 2014 - 2018 | 💵 👶 | A startup that made a series of experimental programming systems and was shut down in 2018.
| [Prune](https://twitter.com/KentBeck/status/634802168508235777) | 2015 | | An internal research project in Facebook. Concluded in it "being promising" but according to them "programmers don't spend that much time manipulating programs compared to all the other things they do. Enabling programmers to do a 50% better job of a task requiring 10% of their time just doesn't make economic sense" (redacted quote).
| [Novella](https://github.com/chrisdone/novella) | 2019 - 2020 | | A structural editor infrastructure, in 2020 author moved on to develop Inflex instead.
| [Expressions of Change](https://www.expressionsofchange.org) | 2017 - 2018 | |
| [Isomorf](https://isomorf.io/#!/) | 2017? | 💵 🌐 👶 λ | A startup developing an in-browser editor for a language that can appear in a syntax of the user's choosing among a few options appearing like different popular programming language
| [Omni](https://github.com/daniel-kun/omni) | 2013 - 2017 | 👶 |
| [Viskell](https://github.com/viskell/viskell) | 2015 - 2017 | λ | Visual programming meets Haskell
| [Zinal](https://gitlab.com/nickcollins/zinal) | 2015 - 2017 | 👶 |
| [Golem](http://xixixao.github.io/Golem/) | 2014 - 2016 | 🎓 📖 ⌨️ 👶 λ ｟ 🌐 | Online tree editor and debugger for [Shem](https://github.com/xixixao/Shem), a functional LISP-like language which compiles to JavaScript
| [Cedalion](http://cedalion.sourceforge.net) | ? - 2013 | 🎓 👶 |

## Blocks Programming Editors

Blocks Programming languages/editors are a specific kind of structural programming editors,
where the code is structured in a manner similar to "lego blocks" supporting "drag and drop" editing.

| System                                     | Properties | Written in
|-------------------------------------------:|:----------:|:-----------
| [Alice](http://www.alice.org)              | 🎓 | Java
| [Hopscotch](https://gethopscotch.com)      | 💵 | ?
| [Microsoft MakeCode](https://makecode.com) | 💵 👶 🌐 | ?
| [Scratch](https://scratch.mit.edu)         | 🎓 文 👶 🌐 | JavaScript
| [Snap](https://snap.berkeley.edu)          | 🎓 文 🌐 | ?

## Spreadsheet-based projects

| System                                                              | Properties | Written in
|--------------------------------------------------------------------:|:----------:|:--------------
| [Flowsheets](http://tinyletter.com/Flowsheets/)                     | | ?
| [Mesh](https://github.com/chrispsn/mesh)                            | | JavaScript
| [Object Spreadsheets](https://sdg.csail.mit.edu/projects/objsheets) | 🎓 | TypeScript

## Other notable projects

Not sure in which category these projects fit in:

| System                                                        | Properties | Description              | Written in
|--------------------------------------------------------------:|:----------:|:-------------------------|:--------------
| [Apparatus](http://aprt.us)                                   | 🎓 🌐 | Hybric diagrams editor | CoffeeScript
| [Cycle.js Dev Tools](https://cycle.js.org)                    | ♡ | Dataflow debugging | TypeScript
| [JSON Editor](https://github.com/json-editor/json-editor.git) | 🌐 | JSON schema-based editor | JavaScript
| [Greenfoot/BlueJ](https://www.greenfoot.org/)                 | 🎓 | Structure-text hybrid | Java

## Resources

### Related lists

- [The whole code catalog](https://futureofcoding.org/catalog/) - An in-depth review of 23 structural and low-code projects by Steve Krouse from 2019. Sponsored by Dark.
- [Gallery of programming UIs](http://alarmingdevelopment.org/?p=1068) - By Jonathan Edwards.
- [Visual Programming Languages - Snapshots](http://blog.interfacevision.com/design/design-visual-progarmming-languages-snapshots/) - By Eric Hosick.

### Community

- [Reddit: /r/nosyntax](https://www.reddit.com/r/nosyntax/) - A subreddit about projectional/structural editing.
- [Future of Coding](https://futureofcoding.org/community) - A Slack-based community with a wider focus.
- Conferences:
  - [LIVE Programming workshop](https://liveprog.org) - An annual workshop at the SPLASH conference mainly focused on live programming.
