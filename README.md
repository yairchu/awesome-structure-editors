# Awesome Structure Editors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A list of structural/projectional code editor projects.

Any comments, suggestions? [Let us know!](https://github.com/yairchu/awesome-structure-editors/issues)

## Foreword

Projectional editing is how almost all document editing applications work nowadays, except for editing source code and text documents, where it is still common to edit plain text files that are parsed to render/compile the result.

This document is a list of projects trying to bring the projectional/structural approach to source code editing.

As evident from the wealth of ongoing and concluded attempts listed below, this problem appears to be either a difficult, or impossible. Hopefully one or more of these projects will succeed in realising it and bringing it to the mainstream!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**

- [Active structural code editor projects](#active-structural-code-editor-projects)
  - [Unreleased Projects](#unreleased-projects)
  - [Blocks Programming Editors](#blocks-programming-editors)
- [Visual code editor projects](#visual-code-editor-projects)
- [Spreadsheet-based projects](#spreadsheet-based-projects)
- [Other notable projects](#other-notable-projects)
- [Related lists](#related-lists)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Active structural code editor projects

This list includes projects which are actively developed or were maintained recently. Currently the bar is set arbitrarily at 2019.

Projects are also summarized with unicode or emoji "flags" (their meanings explained in legend below)

| Project | Flags | Description | Written in | ⭐️ | Updated
|--------:|:-----:|:------------|:---------------|:---|:------------------
| [Unison](https://unisonweb.org) | $ 👶 λ | Code database projected to text-files edited in your text editor of choice. Originally centered around having a projectional editor but pivoted to a cloud programming language | Haskell | 4371 | [2022](https://github.com/unisonweb/unison)
| [Lamdu](http://www.lamdu.org) | ⌨️ 文 👶 λ  | Language with live programming and novel UX for type errors | Haskell | 1750 | [2022](https://github.com/lamdu/lamdu)
| [MPS](https://www.jetbrains.com/mps/) | $ ⌨️ 🔨 | Language workbench for projectional languages | Java | 1302 | [2022](https://github.com/JetBrains/MPS)
| [Dark](https://darklang.com) | $ ⌨️ 🌐 👶 λ | Platform and language as a service for app backends and web | F#, ReScript | 1031 | [2022](https://github.com/darklang/dark)
| [Hazel](http://hazel.org) | 🎓 ⌨️ 🌐 👶 λ | Language with live programming and types holes | Reason | 466 | [2022](https://github.com/hazelgrove/hazel)
| [Sapling](https://github.com/kneasle/sapling) | | ? | Rust | 354 | 2022
| [Fructure](https://fructure-editor.tumblr.com) | ｟ | ? | Racket | 335 | [2020](https://github.com/disconcision/fructure)
| [Cirru](http://cirru.org) | ｟ | A tree editor for ClojureScript | Clojure | 194 | [2022](https://github.com/Cirru/calcit-editor)
| [ProjecturEd](https://github.com/projectured/projectured) | 👨‍👩‍👧‍👦 | General purpose projectional editor | Common Lisp | 125 | 2021
| [Envision](http://dimitar-asenov.github.io/Envision/) | 🎓 👶 | Editor for a Java/C++ like language | C++ | 84 | [2022](https://github.com/dimitar-asenov/Envision)
| [Tofu](https://github.com/Gregoor/tofu) | ☕ | VSCode extension for structured editing of JavaScript and TypeScript | TypeScript | 83 | 2022
| [Subtext](http://www.subtext-lang.org) | 👶 | A serie of inspiring presentations and projects exploring ideas in projectional editing | TypeScript | 82 | [2022](https://github.com/JonathanMEdwards/subtext10)
| [Foundry](https://github.com/int-index/foundry) | λ | A projectional editor for the Morte language | Haskell | 27 | 2022
| [Lisperanto](https://github.com/uprun/lisperanto) | ｟🌐 | IDE for Lisp-like language | JavaScript | 24 | 2022
| [Forest](https://github.com/tehwalris/forest) | ☕ | TypeScript | TypeScript | 18 | 2022
| [Frugel](https://github.com/cdfa/frugel) | 🎓 ⌨️ 👶 λ | A research exploring a novel UX for textual entry of code | Haskell | 6 | 2022
| [Alfa](https://cth.altocumulus.org/~hallgren/Alfa/index.html) | 🎓 λ | An editor for Agda which doesn't allow incorrect code | Haskell | - | 2020
| [OCell](http://kevinmahoney.co.uk/ocell/) | 👶 🌐 | ? | ? | - | 2020

Legend:
* Project structure: $ Commercial, 🎓 Academic
* Target languages: 👶 New language, λ Functional, ｟ Lisp-based, ☕ Javascript/Typescript
* Status:  🔨 Is in some production use
* Target audience: 👨‍👩‍👧‍👦 For everyone (not intended towards programmers)
* Other properties: ⌨️ Text editing like UX, 🌐 Works in browser, 文 Localization support

### Unreleased Projects

* [Roc](https://www.roc-lang.org) - A performance oriented functional programming language [with a structural editor](https://youtu.be/ZnYa99QoznE?t=5864)
* [SplootCode](https://splootcode.io) - A structural editor for Python, aimed towards beginners
* [Dion Systems](https://dion.systems)
* [Programming with Plain Words](https://www.patreon.com/posts/screenshot-with-14865073) - An educational editor for a structured English-like language. No update since 2017 afaik

### Concluded or inactive projects

* [Intentional software](https://en.wikipedia.org/wiki/Intentional_Software) (1990s - 2017) started as a Microsoft project to develop a projectional editor in the late 1990s (see [video from 2000](https://youtu.be/tSnnfUj1XCQ)), which later spun up as an independent company, which later pivoted to develop a language workbench. Despite being founded and self-funded by [a Billionaire](https://en.wikipedia.org/wiki/Charles_Simonyi), it was ultimately acquihired by Microsoft at 2017, with the original projects being canceled (afaik).
* [Eve](https://futureofcoding.org/essays/eve/) (2014 - 2018) was a startup that made a serie of experimental programming systems and shut down in 2018.
* [Prune](https://twitter.com/KentBeck/status/634802168508235777) (2015) was an internal research project in Facebook. Concluded in it being promising but according to them "programmers don't spend that much time manipulating programs compared to all the other things they do ... enabling ... programmers to do a 50% better job ... of a task requiring 10% of their time just doesn't make economic sense"
* [Isomorf](https://isomorf.io/#!/) is a startup developing an in-browser editor for a language that can appear in a syntax of the user's choosing among a few options appearing like different popular programming language. No updates since 2017?
* [Omni](https://github.com/daniel-kun/omni) was declared as on-hold since 2017
* [Zinal](https://gitlab.com/nickcollins/zinal) last updated in 2017

### Blocks Programming Editors

Blocks Programming languages/editors are a specific kind of structural programming editors,
where the code is structured in a manner similar to "lego blocks" supporting "drag and drop" editing.

| System                                     | Flags | Written in
|-------------------------------------------:|:-----:|:-----------
| [Alice](http://www.alice.org)              | 🎓 | Java
| [GP](https://harc.ycr.org/project/gp/)     | 🎓 | ?
| [Hopscotch](https://gethopscotch.com)      | $ | ?
| [Microsoft MakeCode](https://makecode.com) | $ 👶 | ?
| [Scratch](https://scratch.mit.edu)         | 🎓 文 👶 | JavaScript
| [Snap](https://snap.berkeley.edu)          | 🎓 文 | ?

## Visual code editor projects

| System                                        | Flags | Written in
|----------------------------------------------:|:-----:|:-----------
| [Enso](http://www.enso.org)                   | $ 👶 | Haskell
| [Noflo](https://noflojs.org/)                 | ☕ | CoffeeScript
| [Viskell](https://github.com/viskell/viskell) | λ | Java
| [Vlojure](https://vlojure.io)                 | | [Clojure](https://github.com/Ella-Hoeppner/Vlojure)

This list does not include domain-oriented systems like:
[PureData](https://puredata.info),
[MAX](https://cycling74.com/products/max/),
[LabView](http://www.ni.com/en-il/shop/labview.html),
[Simulink](https://www.mathworks.com/products/simulink.html)..

## Spreadsheet-based projects

| System                                                              | Flags | Written in
|--------------------------------------------------------------------:|:-----:|:--------------
| [Flowsheets](http://tinyletter.com/Flowsheets/)                     | | ?
| [Mesh](https://github.com/chrispsn/mesh)                            | | JavaScript
| [Object Spreadsheets](https://sdg.csail.mit.edu/projects/objsheets) | 🎓 | TypeScript

## Other notable projects

Not sure in which category these projects fit in:

| System                                                        | Flags | Description              | Written in
|--------------------------------------------------------------:|:-----:|:-------------------------|:--------------
| [Apparatus](http://aprt.us)                                   | 🎓 | Hybric diagrams editor | CoffeeScript
| [Cycle.js Dev Tools](https://cycle.js.org)                    | | Dataflow debugging | TypeScript
| [JSON Editor](https://github.com/json-editor/json-editor.git) | | JSON schema-based editor | JavaScript
| [Greenfoot/BlueJ](https://www.greenfoot.org/)                 | 🎓 | Structure-text hybrid | Java

## Related lists

* [The whole code catalog](https://futureofcoding.org/catalog/) by Steve Krouse (sponsored by Dark). An in-depth review of 23 structural and low-code projects from 2019
* [Gallery of programming UIs](http://alarmingdevelopment.org/?p=1068) by Jonathan Edwards
* [Visual Programming Languages - Snapshots](http://blog.interfacevision.com/design/design-visual-progarmming-languages-snapshots/) by Eric Hosick
