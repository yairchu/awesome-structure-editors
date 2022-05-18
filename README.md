# Awesome Structure Editors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A list of structural/projectional code editor projects.

Any comments, suggestions? [Let us know!](https://github.com/yairchu/awesome-structure-editors/issues)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Contents

- [Foreword](#foreword)
- [Active structural code editor projects](#active-structural-code-editor-projects)
  - [Unreleased Projects](#unreleased-projects)
  - [Concluded or inactive projects](#concluded-or-inactive-projects)
  - [Blocks Programming Editors](#blocks-programming-editors)
- [Spreadsheet-based projects](#spreadsheet-based-projects)
- [Other notable projects](#other-notable-projects)
- [Related lists](#related-lists)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Foreword

Projectional editing is how almost all document editing applications work nowadays, except for editing source code and text documents, where it is still common to edit plain text files that are parsed to render/compile the result.

This document is a list of projects trying to bring the projectional/structural approach to source code editing.

As evident from the wealth of ongoing and concluded attempts listed below, this problem appears to be either difficult, or impossible. Hopefully one or more of these projects will succeed in realising it and bringing it to the mainstream!

## Active structural code editor projects

This list includes projects which are actively developed or were maintained recently. Currently the bar is set arbitrarily at 2020.

Project properties are summarized using unicode/emoji "flags":
- Project structure: 💵 Commercial, 🎓 Academic
- UX: 📖 Uses text files, ⤴️ Visual programming, ⌨️ Text editing like UX
- Target languages: 👶 New language, λ Functional, ｟ Lisp-based, ☕ JavaScript/TypeScript
- Other: 🔨 Is in some production use, 🌐 Works in browser, 👨‍👩‍👧‍👦 Not intended for programmers, 文 Localization support

| Project | Properties | Description | Written in | ⭐️ | Updated
|--------:|:----------:|:------------|:----------:|:--:|:-------:
| [Enso](https://enso.org) | 💵 📖 ⤴️ 👶 λ | Hybrid visual+textual programming language | Scala, Rust | [5506](https://github.com/enso-org/enso) | 2022
| [Unison](https://unisonweb.org) | 💵 📖 👶 λ | Code database projected to text-files edited in your text editor of choice. Originally centered around having a projectional editor, but pivoted to creating a cloud programming language first | Haskell | [4381](https://github.com/unisonweb/unison) | 2022
| [Lamdu](http://www.lamdu.org) | ⌨️ 👶 λ 文 | Language with live programming and novel UX for type errors | Haskell | [1753](https://github.com/lamdu/lamdu) | 2022
| [MPS](https://www.jetbrains.com/mps/) | 💵 ⌨️ 🔨 | Language workbench for projectional languages | Java | [1305](https://github.com/JetBrains/MPS) | 2022
| [Dark](https://darklang.com) | 💵 ⌨️ 👶 λ 🌐 | Platform and language as a service for app backends and web | F#, ReScript | [1036](https://github.com/darklang/dark) | 2022
| [Hazel](http://hazel.org) | 🎓 ⌨️ 👶 λ 🌐 | Language with live programming and typed holes | Reason | [466](https://github.com/hazelgrove/hazel) | 2022
| [Sapling](https://github.com/kneasle/sapling) | ⌨️ | Vim/Kakoune-inspired modal structured editor for existing languages | Rust | 354 | 2022
| [Fructure](https://fructure-editor.tumblr.com) | ｟ | ? | Racket | [344](https://github.com/disconcision/fructure) | 2020
| [Cirru](http://cirru.org) | ｟ | A tree editor for ClojureScript | Clojure | [195](https://github.com/Cirru/calcit-editor) | 2022
| [ProjecturEd](https://github.com/projectured/projectured) | 👨‍👩‍👧‍👦 | General purpose projectional editor | Common Lisp | 125 | 2021
| [Vlojure](https://vlojure.io) | ⤴️ ｟ 🌐 | A novel visual UX for ClojureScript | Clojure | [112](https://github.com/Ella-Hoeppner/Vlojure) | 2022
| [Envision](http://dimitar-asenov.github.io/Envision/) | 🎓 👶 | Editor for a Java/C++ like language | C++ | [84](https://github.com/dimitar-asenov/Envision) | 2022
| [Tofu](https://github.com/Gregoor/tofu) | ☕ | VSCode extension for structured editing of JavaScript and TypeScript | TypeScript | 83 | 2022
| [Holbert](http://liamoc.net/holbert) | 🎓 🌐 | A graphical interactive proof assistant designed for education | Haskell | [82](https://github.com/liamoc/holbert) | 2022
| [Subtext](http://www.subtext-lang.org) | 👶 | A series of inspiring presentations and projects exploring ideas in projectional editing | TypeScript | [82](https://github.com/JonathanMEdwards/subtext10) | 2022
| [Foundry](https://github.com/int-index/foundry) | λ | A projectional editor for the Morte language | Haskell | 28 | 2022
| [Lisperanto](https://github.com/uprun/lisperanto) | ｟ 🌐 | IDE for Lisp-like language | JavaScript | 24 | 2022
| [Forest](https://github.com/tehwalris/forest) | ☕ | A prototype tree editor for TypeScript | TypeScript | 20 | 2022
| [Frugel](https://github.com/cdfa/frugel) | 🎓 ⌨️ 👶 λ | A research exploring a novel UX for textual entry of code | Haskell | 9 | 2022
| [Alfa](https://cth.altocumulus.org/~hallgren/Alfa/index.html) | 🎓 λ | An editor for Agda which doesn't allow incorrect code | Haskell | - | 2020
| [OCell](http://kevinmahoney.co.uk/ocell/) | 👶 🌐 | ? | ? | - | 2020

### Unreleased Projects

- [Roc](https://www.roc-lang.org) - A performance oriented functional programming language [with a structural editor](https://youtu.be/ZnYa99QoznE?t=5864).
- [SplootCode](https://splootcode.io) - A structural editor for Python, aimed towards beginners.
- [Dion Systems](https://dion.systems)
- [Programming with Plain Words](https://www.patreon.com/posts/screenshot-with-14865073) - An educational editor for a structured English-like language. No update since 2017 afaik.

### Concluded or inactive projects

- [Intentional software](https://en.wikipedia.org/wiki/Intentional_Software) - 1990s to 2017. Started as a Microsoft project to develop a projectional editor in the late 1990s (see [video from 2000](https://youtu.be/tSnnfUj1XCQ)), which later spun up as an independent company, which later pivoted to develop a language workbench. Despite being founded and self-funded by [a Billionaire](https://en.wikipedia.org/wiki/Charles_Simonyi), it was ultimately acquired by Microsoft at 2017, with the original projects being cancelled (afaik).
- [Eve](https://futureofcoding.org/essays/eve/) - 2014 to 2018. A startup that made a series of experimental programming systems and was shut down in 2018.
- [Prune](https://twitter.com/KentBeck/status/634802168508235777) - 2015. An internal research project in Facebook. Concluded in it being promising but according to them "programmers don't spend that much time manipulating programs compared to all the other things they do. Enabling programmers to do a 50% better job of a task requiring 10% of their time just doesn't make economic sense" (redacted quote).
- [Isomorf](https://isomorf.io/#!/) - A startup developing an in-browser editor for a language that can appear in a syntax of the user's choosing among a few options appearing like different popular programming language. No updates since 2017?
- [Omni](https://github.com/daniel-kun/omni) - Declared as on-hold since 2017.
- [Viskell](https://github.com/viskell/viskell) - Visual programming meets Haskell. Last updated in 2017.
- [Zinal](https://gitlab.com/nickcollins/zinal) - Last updated in 2017.

### Blocks Programming Editors

Blocks Programming languages/editors are a specific kind of structural programming editors,
where the code is structured in a manner similar to "lego blocks" supporting "drag and drop" editing.

| System                                     | Properties | Written in
|-------------------------------------------:|:----------:|:-----------
| [Alice](http://www.alice.org)              | 🎓 | Java
| [Hopscotch](https://gethopscotch.com)      | 💵 | ?
| [Microsoft MakeCode](https://makecode.com) | 💵 👶 | ?
| [Scratch](https://scratch.mit.edu)         | 🎓 文 👶 | JavaScript
| [Snap](https://snap.berkeley.edu)          | 🎓 文 | ?

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
| [Apparatus](http://aprt.us)                                   | 🎓 | Hybric diagrams editor | CoffeeScript
| [Cycle.js Dev Tools](https://cycle.js.org)                    | | Dataflow debugging | TypeScript
| [JSON Editor](https://github.com/json-editor/json-editor.git) | | JSON schema-based editor | JavaScript
| [Greenfoot/BlueJ](https://www.greenfoot.org/)                 | 🎓 | Structure-text hybrid | Java

## Related lists

- [The whole code catalog](https://futureofcoding.org/catalog/) - An in-depth review of 23 structural and low-code projects by Steve Krouse from 2019. Sponsored by Dark.
- [Gallery of programming UIs](http://alarmingdevelopment.org/?p=1068) - By Jonathan Edwards.
- [Visual Programming Languages - Snapshots](http://blog.interfacevision.com/design/design-visual-progarmming-languages-snapshots/) - By Eric Hosick.
