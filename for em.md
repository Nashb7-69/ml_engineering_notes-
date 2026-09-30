# From "It Works" to "It's Professional"

## The Complete Flutter Professional Practice Course

### Instructor's Master Notes: a 3-Hour, Theory-Only Session

_These notes are written for YOU, the instructor. They are not a script to read to students. Each module gives you the ideas, the reasoning behind them, the analogies, the traps, the questions to ask, and model answers to the questions students are likely to throw back at you. Talk from them, paraphrase them, argue with them. Everything is theory: no live coding is needed. You can present from your laptop using a blank whiteboard app, a few diagrams (I've included ASCII sketches you can redraw), and the official documentation pages listed in the appendix._

---

## 0. How to Use These Notes

### Legend

- **SAY:** a key sentence or idea worth delivering close to verbatim.
- **ASK:** a question to put to the room. Wait. Let silence do the work.
- **BOARD:** something worth drawing or writing where they can see it.
- **PITFALL:** a common misconception or mistake. Students remember mistakes better than rules.
- **CUT:** what to drop if you are running late.
- **EXPAND:** what to add if the room is engaged and you have time.
- **VERIFY:** a detail that changes over time (store policies, package versions, tool defaults). Check the official page before you state it as fact.

### Timing map (180 minutes total)

|Block|Topic|Minutes|Clock (start at 0:00)|
|---|---|---|---|
|Opening|Framing: why "it works" is not enough|10|0:00 to 0:10|
|Module 1|Architecture and State Management|30|0:10 to 0:40|
|Module 2|Mobile App Security|25|0:40 to 1:05|
|Break||10|1:05 to 1:15|
|Module 3|Networking, APIs, Data and Offline|25|1:15 to 1:40|
|Module 4|Quality: Testing, CI/CD, Engineering Habits|20|1:40 to 2:00|
|Module 5|Performance|15|2:00 to 2:15|
|Break||10|2:15 to 2:25|
|Module 6|Shipping and Watching|15|2:25 to 2:40|
|Module 7|Careers, Portfolio, Interviews|15|2:40 to 2:55|
|Closing|Wrap-up and send-off|5|2:55 to 3:00|

If you like to "yap" (and you said you do), treat the minute counts as _minimums for the core story_. Each module has an **EXPAND** section you can pull from. The total content here is comfortably more than three hours if you use everything, so you have room to choose.

### The one-sentence spine of the whole course

> **Software is not a thing you build once. It is a thing you keep alive, and everything professional is about making that survivable.**

Every module is the same argument from a different angle:

1. Architecture: keep _change_ cheap.
2. Security: keep _users_ safe.
3. Networking: keep the app _working when the world doesn't_.
4. Testing: keep _yourself_ fearless.
5. Performance: keep the app _pleasant_.
6. Shipping: keep the app _observable_.
7. Career: keep _yourself_ growing.

Repeat the spine at the start of each module in one line ("Module 3 is about keeping the app alive when the network is not"). It gives students a rope to hold.

### Teaching principles for this session

- **Theory lands when it is attached to pain.** Start each module with a _failure story_ (a broken app, a leaked key, a crashed launch), then reveal the concept as the cure.
- **Ask before you tell.** A student who has guessed an answer (even wrongly) learns the correct answer roughly twice as well.
- **Trade-offs, not commandments.** Never say "you must use X." Say "X buys you this and costs you that." This is the single most professional habit you can model.
- **Connect to their projects.** Every few minutes, say: "Think about your own project right now. Where does this apply?"
- **Admit uncertainty out loud.** When you say "this depends, and honestly people disagree," you give them permission to think instead of memorize.

### Pre-session checklist (10 minutes of preparation)

- Open these tabs in advance: docs.flutter.dev (Architecture, Testing, Performance, Deployment sections), owasp.org (Mobile Top 10 and MASVS), and one crash-reporting dashboard screenshot if you have one.
- Have a whiteboard or drawing tool ready for diagrams.
- Prepare a few _anonymized_ examples of common student-project mistakes you have seen. Real examples beat invented ones.
- Decide in advance which two things you will CUT if you run 15 minutes late (suggestion: the Riverpod deep dive and the GraphQL/gRPC aside).

---

## Opening (10 minutes): Why "It Works" Is Not Enough

### Goal of this block

Change the students' definition of "done." By minute ten they should feel slightly uncomfortable about their own finished projects, in a motivating way.

### Talking points

**1. Congratulate them for real.** They built something from nothing: screens, a database, an API. Most people who say "I want to learn programming" never get here. Let them feel that for thirty seconds. This makes the next part land as guidance, not criticism.

**2. Then reset the bar.**

**SAY:** "Working software is the entry ticket to this profession. It is not the profession. The profession begins when someone else has to read your code, when a thousand people use it at once, when the network fails, when an attacker looks at it, and when you come back to it in six months and cannot remember why you wrote it that way."

**3. The lifetime-cost idea.** Most of the cost of software is not in _writing_ it. It is in _maintaining_ it. Industry folklore (and several studies, with varying numbers) puts maintenance at well over half of a system's total lifetime cost, and often far more. So professionalism means: **write code that is cheap to change, cheap to understand, and cheap to trust.**

**4. Three questions to leave hanging.** Put these on the board and return to them at the end:

- If a stranger tried to break your app, how long would it take them?
- If the internet dropped right now, what would your user see?
- If a new developer joined tomorrow, how long until they could safely change something?

**ASK:** "Which of those three questions scares you most about your own project?" Take two or three answers. Do not comment much. You are collecting fears you will address later.

**5. Preview the map.** Show the seven modules in one breath. Tell them you will not teach new widgets. You will teach how professionals _think_.

**EXPAND:** Tell a short story of a real-world software failure caused by ordinary mistakes (a leaked API key that ran up a huge cloud bill; an app update that broke for users on old versions; a rollout that crashed on launch for one device family). Keep it to two minutes and keep it factual, without naming individuals.

---

## Module 1 (30 minutes): Architecture and State Management

**Spine line:** _Architecture is about making change cheap._

### 1.0 Failure story to open with (2 min)

Describe the typical student project screen: one widget file, 600 lines. Inside `build()` there is an HTTP call, JSON parsing, a `setState` on six variables, an `if` statement deciding which error text to show, and a hard-coded API URL. It works. Now ask:

**ASK:** "Your lecturer says: switch from this REST API to a different backend. How many places do you have to edit? How sure are you that you found them all?"

That fear is the reason architecture exists.

### 1.1 What "architecture" actually means (3 min)

**Plain definition:** architecture is the set of decisions that are _expensive to change later_. Which layers exist, who is allowed to know about whom, where state lives, how data flows.

**Two useful metaphors (pick one):**

- _The house without a blueprint._ You can add rooms, but eventually you discover the wall you want to move is load-bearing.
- _The kitchen._ A restaurant kitchen has stations: prep, grill, plating, dishwashing. Not because the cook can't do everything, but because when the restaurant grows from 10 to 200 customers, stations are the only thing that scales.

**Technical debt.** Introduce this term. Technical debt is the accumulated cost of shortcuts. Like financial debt, it is not always bad (a startup borrowing time to launch is rational), but **debt with no repayment plan eventually bankrupts the project.** Interest is paid every time someone has to work around the mess.

**The "Big Ball of Mud."** A famous 1997 paper (Foote and Yoder) named the most common architecture in the world: _no architecture._ It is not caused by stupid people. It is caused by ordinary pressure and small shortcuts adding up. Say this to reassure them: their messy first project is normal, and the goal is awareness, not shame.

**PITFALL:** Students hear "architecture" and think "more folders and more files." Correct this early: architecture is about _responsibilities and dependencies_, not folder names.

### 1.2 Flutter fundamentals you need for the architecture story (4 min)

Quickly recall the mental model, because state management and performance both depend on it.

**Everything is a widget, but widgets are only descriptions.** A widget is an _immutable configuration_: "here is what I want on screen, with these properties." It is cheap to create and throw away.

**Flutter keeps three parallel trees:**

1. **Widget tree**: the immutable descriptions you write. Rebuilt often, on purpose.
2. **Element tree**: the long-lived instances that sit in specific positions in the tree. Elements decide whether to reuse or replace what's underneath when a widget changes. This is where "state" lives for `StatefulWidget`s.
3. **RenderObject tree**: the objects that do layout and painting.

**BOARD:** draw three columns with arrows: Widget (blueprint) → Element (the actual building site) → RenderObject (the physical structure).

**Why this matters for the course:**

- Rebuilding widgets is _designed to be cheap_. That's why Flutter lets you rebuild freely. The cost appears only when rebuilds trigger expensive work (Module 5).
- State must live _somewhere that survives rebuilds_. Widgets are discarded; Elements/State objects persist.
- `BuildContext` is really a handle to an Element: your position in the tree. That's why you can look _up_ the tree for inherited data.

**StatefulWidget lifecycle (worth naming, briefly):** `createState` → `initState` → `didChangeDependencies` → `build` → (`didUpdateWidget` / `setState` → `build` again) → `deactivate` → `dispose`. The two most important lessons: put one-time setup in `initState`, and clean up in `dispose`. This will come back in the memory-leak discussion.

### 1.3 Separation of concerns and layers (5 min)

**The single most important principle in software design:** each part of the system should have **one reason to change.** (This is the "single responsibility" idea.)

**BOARD:** draw this diagram.

```
   +---------------------------------------------+
   |  UI LAYER                                   |
   |  Widgets (Views) + ViewModels / State       |
   |  "What does the user see and do?"           |
   +----------------------+----------------------+
                          |  asks for data / sends actions
                          v
   +---------------------------------------------+
   |  (optional) DOMAIN LAYER                    |
   |  Use cases / business rules                 |
   |  "What are the rules of our app?"           |
   +----------------------+----------------------+
                          |
                          v
   +---------------------------------------------+
   |  DATA LAYER                                 |
   |  Repositories  ->  Services / Data sources  |
   |  (API client, local DB, secure storage)     |
   |  "Where does data come from and go to?"     |
   +---------------------------------------------+
```

**Explain each layer by its ignorance:**

- The **UI layer** knows how to draw and respond to taps. It must _not_ know whether data came from REST, GraphQL, or a file.
- The **domain layer** (optional; use it when business rules are rich or shared) knows the rules ("a user can't book two overlapping appointments"). It must not know about widgets _or_ about HTTP.
- The **data layer** knows how to fetch and store. It must not know which screen wants the data.

**SAY:** "A good layer is defined by what it refuses to know."

**Why this pays off (the four dividends):**

1. **Replaceability.** Swap the API, keep the screens.
2. **Testability.** Test rules without launching an emulator.
3. **Parallel work.** Two people can work on UI and data without colliding.
4. **Readability.** A newcomer knows where to look.

**The Flutter team's own guidance.** The official "App architecture" guide recommends this same shape: a UI layer (views + view models), a data layer (repositories + services), and an optional domain layer for complex logic. It emphasizes _repositories as the single source of truth_ for a type of data, _unidirectional data flow_, and _immutable state_. **VERIFY** the current wording on docs.flutter.dev, but the ideas have been stable.

### 1.4 The patterns you'll hear about (6 min)

**MVC → MVP → MVVM: the family tree.** All are answers to "how do we separate the screen from the logic?" You don't need the history in detail, just this: they differ in _how the middle piece talks to the view_.

**MVVM in Flutter, in plain words.**

- **Model**: your data and rules.
- **View**: widgets. Dumb on purpose. They render state and forward user actions.
- **ViewModel**: holds the state a screen needs, exposes actions, talks to repositories. It never references widgets.

The view _observes_ the view model. When the view model's state changes, the view rebuilds.

**The Repository pattern.** A repository is a class that _hides where data comes from_. The UI asks `userRepository.getProfile()`; it doesn't know if that came from the network, a cache, or a local database. This is the seam that makes offline-first possible (Module 3), and testing easy (you can hand the view model a fake repository).

**DTO vs domain model.** A DTO (data transfer object) mirrors the _shape of the API response_, ugly field names and all. A domain model is the _shape your app wants to think in._ Convert at the boundary (in the repository). Why? Because when the backend team renames a field, only one mapping function changes, not fifty widgets.

**Dependency Injection (DI) and Dependency Inversion.**

- _Dependency injection_ means a class receives the things it needs (from the outside) instead of creating them itself. `UserViewModel(this.userRepository)` rather than `UserViewModel() { repo = UserRepository(); }`.
- _Dependency inversion_ (the "D" in SOLID) means high-level code depends on **abstractions** (an interface like `UserRepository`), not on concrete details (like `HttpUserRepository`).
- Why it matters: you can inject a fake in tests and a real one in production. In Flutter people achieve DI with Provider, Riverpod, `get_it`, or plain constructor passing. **The tool is less important than the principle.**

**Clean Architecture (Robert C. Martin).** Concentric circles: entities and use cases at the center, adapters and frameworks on the outside. **The Dependency Rule: source-code dependencies point inward only.** Inner circles know nothing about outer ones. Your business rules should not `import 'package:flutter/material.dart'`.

**SOLID in one breath.**

- **S**ingle responsibility: one reason to change.
- **O**pen/closed: extend behavior without rewriting existing code.
- **L**iskov substitution: subtypes must be usable wherever the parent is.
- **I**nterface segregation: small, focused interfaces beat one giant one.
- **D**ependency inversion: depend on abstractions.

**PITFALL: over-engineering.** Say this with weight:

**SAY:** "Architecture has a cost. Every layer is more files, more boilerplate, more ceremony. For a to-do app, full Clean Architecture is hiring a construction crew to hang a picture frame. The professional skill isn't knowing the patterns. It's knowing how much structure _this_ project deserves."

A useful rule of thumb: **start simple, and add structure at the moment the pain appears** (the second time you copy-paste, the first time a test is impossible to write). Also mention the acronyms **YAGNI** ("you aren't gonna need it"), **KISS** ("keep it simple"), and **DRY** ("don't repeat yourself"), and that DRY is often over-applied: duplication is cheaper than the _wrong abstraction_.

**Folder structure: two schools.**

- _Layer-first_: `/models`, `/views`, `/services`. Easy at the start, painful at scale (one feature is scattered everywhere).
- _Feature-first_: `/features/login/{ui,logic,data}`, `/features/profile/...`. A feature lives together. Most teams prefer this as apps grow.

**Architecture Decision Records (ADRs).** A one-page note: "We chose Riverpod because... We considered Bloc but... The consequence is...". It's a professional habit that saves teams from re-arguing old decisions. Recommend it for their capstone documentation.

**EXPAND:** Explain immutability. Immutable state objects (fields are `final`; changes create a _new_ object) make change detection trivial and eliminate a class of bugs where two parts of the app mutate the same object. Mention that packages like `freezed` and `equatable` help with value equality and copy-with. Explain _why equality matters_: state libraries decide whether to rebuild by comparing old and new state.

### 1.5 State management: the real problem (8 min)

**What is state?** Everything in your app that can change over time and affects what the user sees: the logged-in user, cart contents, a loading spinner, a text field's current text, a selected tab.

**The Flutter docs draw a useful distinction:**

- **Ephemeral (local) state**: belongs to one widget and nobody else cares (current tab index, animation progress, a form field's text). Use `setState` or a `StatefulWidget`. _Don't_ reach for a library.
- **App (shared) state**: needed by many parts of the app, or must survive screen changes (auth session, cart, settings). This is where state management libraries enter.

**PITFALL:** using a heavyweight library for ephemeral state, or using `setState` and callbacks for app state. Both are mismatches.

**The core problem, said simply:**

**SAY:** "The hard part of UI programming is not drawing screens. It's keeping what the user _sees_ consistent with what is _true_. Most UI bugs are the screen showing something that is no longer real."

**The core idea: UI = f(state).** The screen is a _function_ of state. Change the state, and the framework re-runs the function. This is why Flutter (and React, and SwiftUI) feel similar. Then the real question becomes: _where does state live, who is allowed to change it, and how does the UI find out?_

**Key concepts to name:**

- **Single source of truth**: each piece of data has _one_ owner. Copies drift apart and cause bugs.
- **Lifting state up**: when two widgets need the same state, move it to their nearest common ancestor.
- **Unidirectional data flow**: state flows _down_ to the UI; events flow _up_ from the UI. It makes behavior traceable ("who changed this?" always has one answer).
- **Derived state**: don't store what you can compute. Store `items`; compute `total`. Storing both invites inconsistency.
- **Async state has three faces**: loading, data, error. A professional app models all three explicitly, always.

**The ladder of options, from lightest to heaviest:**

**`setState`.** Built in. Perfect for ephemeral state. Its limit is that sharing state across distant widgets means passing it down through constructors ("prop drilling") or callbacks.

**`InheritedWidget` and `ValueNotifier`/`ChangeNotifier`.** Flutter's built-in primitives. `InheritedWidget` lets descendants read data from above and rebuild when it changes. Most libraries below are friendlier wrappers around these ideas.

**Provider.** Places objects in the tree and lets descendants read them. Typically paired with `ChangeNotifier` (which calls `notifyListeners()` to trigger rebuilds). Strengths: small, approachable, officially recommended for years as a starting point. Weaknesses: depends on the widget tree (needs `BuildContext`), easy to misuse (reading versus watching), and can get loose in large apps. Useful API distinction: `context.watch` (rebuild when it changes), `context.read` (get it once, don't rebuild, use in callbacks), and `context.select` (rebuild only when a specific part changes).

**Riverpod.** Created by the same author as Provider, designed to fix Provider's limits. Providers are declared globally but hold no state themselves (state lives in a container), it's compile-time safer, doesn't depend on the widget tree, handles async natively (loading/data/error), supports auto-disposal and "families" (parameterized providers), and is very testable via overrides. Cost: a steeper learning curve and its own vocabulary (`ref.watch`, `ref.read`, `ref.listen`, notifiers). **VERIFY** current API style (code generation vs. manual providers has been evolving).

**Bloc / Cubit.** Based on streams. **Cubit** is the simple form: methods that `emit` new states. **Bloc** adds _events_: the UI sends an event, the bloc maps it to a state (or a series of states). Strengths: very explicit, traceable, great for large teams and for logging every transition. Weaknesses: boilerplate and ceremony. **Analogy:** a strict bureaucracy where every request is a form and every response is a stamped document. Annoying for small offices, a blessing for a big organization. Key widgets: `BlocProvider`, `BlocBuilder` (rebuild UI), `BlocListener` (one-off side effects like showing a snackbar), and `buildWhen` (limit rebuilds).

**Others.** GetX (popular, convenient, but widely criticized for mixing concerns and encouraging global state; mention it neutrally as something students will encounter in tutorials), MobX, Redux-style, signals-style libraries. Name them so students aren't surprised, then move on.

**Comparison table to put on the board:**

||setState|Provider|Riverpod|Bloc/Cubit|
|---|---|---|---|---|
|Learning curve|Lowest|Low|Medium|Medium to high|
|Boilerplate|None|Low|Low to medium|Medium to high|
|Testability|Poor|Good|Very good|Very good|
|Async handling|Manual|Manual|Built in|Explicit states|
|Best for|Local UI state|Small/medium apps|Medium/large, flexible teams|Large teams needing strict structure|

**The honest decision framework:**

**SAY:** "The best state management library is the one your team understands and applies _consistently_. A tidy app in Provider beats a chaotic app in Bloc. Don't chase the trendy one. Understand the _problem_ they all solve, and any of them becomes easy to learn."

Suggest a practical rule for their next project: _if you're alone or the app is small, start with Provider or Riverpod; if you join a large team, use whatever the team uses._

**Anti-patterns to name (with the fix):**

- **Business logic inside widgets.** Fix: move it to a view model/notifier/bloc.
- **God view model**: one class managing the whole app. Fix: split by feature.
- **Global mutable singletons** that anything can change. Fix: expose state through a controlled owner.
- **Duplicated state** (the same data stored in two places). Fix: single source of truth.
- **Using `BuildContext` after an `await`.** The widget may be gone from the tree. Fix: check `mounted` (or `context.mounted`) before using context after async gaps. The `use_build_context_synchronously` lint exists for exactly this.
- **Impossible states.** Booleans like `isLoading`, `hasError`, `data` can be combined in nonsense ways (loading _and_ error?). Fix: model state as a sealed class or union: `Loading`, `Success(data)`, `Failure(error)`. _"Make impossible states impossible"_ is a great slogan.
- **Doing work in `build()`.** `build` can run many times per second. Fix: keep it pure, cheap, and free of side effects.

### 1.6 Discussion and wrap-up (2 min)

**ASK:** "Open your own project in your mind. If I asked you to change the data source tomorrow, how many files would you have to touch? What does that number tell you?"

**ASK:** "Which of your variables is _ephemeral_ and which is _app-wide_? Are they managed the same way?"

### Anticipated student questions (with model answers)

**"Which state management should I learn first?"** Learn `setState` deeply first (it teaches you what the framework does). Then learn one library properly, Provider or Riverpod for most beginners. What transfers between libraries is the _concepts_ (single source of truth, unidirectional flow, immutability), and those are worth more than any syntax.

**"Is Clean Architecture required for a job?"** No. It's a vocabulary many teams use, and knowing it helps you read their code. What employers really want to see is that you can _separate concerns and explain why_.

**"Won't all these layers slow my app down?"** Not measurably. Layers cost developer typing time, not runtime performance. The runtime costs in Flutter apps come from things like heavy rebuilds, large images, and blocking the UI thread.

**"My app is small. Should I skip all this?"** Skip the _ceremony_, keep the _principles_. Even in a small app: don't put HTTP calls in widgets, don't scatter API URLs, and model loading/error states.

**CUT (if late):** the Riverpod/Bloc details; keep the comparison table and the decision framework. **EXPAND (if time):** live-narrate (no code) how a login flow moves through the layers: button tap → view model action → repository → API service → response → DTO to domain model → state change → UI update. Walking a single flow end to end teaches more than any diagram.

---

## Module 2 (25 minutes): Mobile App Security

**Spine line:** _Security is about keeping users safe, including from your own mistakes._

### 2.0 Open with a failure story (2 min)

Pick one and tell it plainly:

- A developer commits a cloud API key to a public repository. Automated bots scan public repositories constantly; within minutes the key is used to run up a very large bill or steal data.
- A team stores auth tokens in plain preferences. Anyone who backs up or inspects a rooted device gets every user's account.
- A database backend is left with permissive rules ("anyone can read and write") because "we'll fix it before launch." It never gets fixed, and user data is exposed.

**ASK:** "What do these three stories have in common?" (Answer to steer toward: none of them required a genius attacker. They were ordinary, preventable mistakes.)

### 2.1 The mindset shift (3 min)

**Flip the question.** Developers ask "how will users use this?" Security thinkers ask "**how would someone abuse this?**"

**The foundational principle:**

> **Anything that lives on the user's device belongs to the user, not to you.**

The phone is not your territory. It's a potentially hostile environment. The device may be rooted or jailbroken, infected with malware, or held by a curious teenager with a decompiler. Your app file can be downloaded by anyone from the store and taken apart.

**Vocabulary students should know (a 60-second glossary):**

- **CIA triad**: **C**onfidentiality (only the right people can read it), **I**ntegrity (nobody can silently change it), **A**vailability (it works when needed). Every security question maps to one of these.
- **Threat model**: a structured answer to "who might attack, what do they want, and how could they get it?" Even a five-minute version helps.
- **Attack surface**: the sum of all the places an attacker can interact with your system (screens, APIs, storage, deep links, permissions, dependencies).
- **Defense in depth**: layered protections, so one failure doesn't mean total failure.
- **Least privilege**: give every component (and every person, and every token) the minimum access it needs.
- **STRIDE** (optional, for the curious): Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege: a checklist for thinking about threats.

**BOARD:** draw four boxes: _Device_, _App_, _Network_, _Server_. Ask students to call out where an attacker could stand. (Answer: all four.) This map organizes the rest of the module.

### 2.2 Device and app: storing things safely (6 min)

**Classify your data first.** Before deciding _how_ to store, decide _what it is_:

- **Harmless** (theme choice, last-opened tab): plain local storage is fine.
- **Sensitive** (tokens, personal information, health, financial): must be protected.
- **Secret** (passwords, private keys): should ideally _never_ be stored on the device at all.

**Why `SharedPreferences` is wrong for tokens.** It stores data in a plain, readable file (on Android, an XML file in the app's private directory; on iOS, the user defaults plist). It's designed for preferences like "dark mode: on." "Private directory" protects against _other apps_ on a normal device, but not against rooting, device backups, forensic tools, or a malicious person holding the phone.

**The right tool: platform secure storage.** iOS has the **Keychain**; Android has the **Keystore** system (hardware-backed on most modern devices). In Flutter this is commonly accessed through a secure-storage package (`flutter_secure_storage` is the well-known one). **VERIFY** the current implementation details of the package, because how it wraps the Android Keystore has changed across versions. Rule of thumb:

**SAY:** "If losing it would hurt a person, it belongs in secure storage, or better, it doesn't belong on the device at all."

**Do not store passwords.** Store a **short-lived access token** and (optionally) a **refresh token**. If the device is compromised, a short-lived token limits the damage. This leads to the token lifecycle:

- **Access token**: short life (minutes). Sent with each API request.
- **Refresh token**: longer life. Used _only_ to get a new access token. Protect it more carefully, and let the server revoke it (for example on logout or suspected theft).
- **Logout should actually invalidate the session server-side**, not only delete the token locally.

**JWTs: a common misunderstanding.** A JSON Web Token has three parts (header, payload, signature). The payload is **encoded, not encrypted**. Anyone holding the token can read the contents. **Never put secrets in a JWT payload.** The signature only proves the server issued it and it wasn't altered.

**Biometrics.** Fingerprint and face unlock (via `local_auth`) confirm _the person at the phone is the owner_. They're a convenience layer to protect access to the app or to a stored key, not a replacement for server-side authentication.

**Local databases.** A regular SQLite file is readable on a rooted device. If you store sensitive records locally, consider encrypting the database (SQLCipher is the known approach) and keep the encryption key in secure storage. Better still: store less.

**Other device-level leaks that students forget:**

- **Logging.** `print()` statements with tokens or personal data end up in device logs. Strip or gate logs in release builds.
- **Screenshots and the app switcher.** Sensitive screens can be captured or shown in the recent-apps preview (Android has `FLAG_SECURE` to block this).
- **Clipboard.** Other apps may read what you copy; avoid copying secrets.
- **Backups.** On Android, allowing backup can expose app data; review the `allowBackup` setting for sensitive apps.
- **Permissions.** Ask only for what you need (least privilege), and explain _why_ at the moment of asking.

### 2.3 The app's secrets: API keys in the client (3 min)

This surprises students, so slow down.

**PITFALL:** "I put the key in my Dart code and nobody sees the code." Your compiled app is a file anyone can download. Strings, endpoints, and structure inside it can be extracted with common tools. Flutter compiles Dart ahead-of-time to native code, which is _harder_ to read than a JavaScript bundle, but it is not a vault, and tools exist specifically for analyzing Flutter binaries.

**SAY:** "A secret inside a client app is not a secret. It's a public key with a private name."

**The professional pattern: the backend-for-frontend.** Keep powerful secrets on **your server**. The app talks to your server; your server talks to the third-party service. Now the server is a guard at the gate. It can:

- authenticate who is asking,
- enforce rate limits and quotas,
- log and audit usage,
- rotate or revoke keys without shipping an app update.

**Distinguish two kinds of "keys":**

- **Public identifiers** (some map or analytics keys are designed to be embedded, but you can restrict them by app signature, bundle ID, or allowed domains). Fine, _if restricted_.
- **Secret keys** (a cloud provider's admin key, a payment secret, an AI provider's key). **Never** ship these in the app.

**Environment configuration.** `--dart-define` and env files keep config out of source control, but be honest with students: they **do not make the value secret** once it's compiled into the app. They keep it out of your Git history, and no more.

**Git hygiene.** Never commit keys, keystores, or `.env` files. Use `.gitignore`. If a secret is ever committed, **rotate it** (assume it's compromised); deleting the file in a later commit does not remove it from history.

### 2.4 The network: protecting the conversation (3 min)

- **HTTPS everywhere.** Non-negotiable. It provides encryption and server authentication. Both Android and iOS actively discourage or block plain HTTP by default.
- **Never disable certificate validation "to make it work in testing."** The line `badCertificateCallback => true` shipped to production is one of the most common real-world vulnerabilities. It silently turns HTTPS into decoration.
- **The man-in-the-middle attack.** Someone tricks the device into trusting a rogue certificate authority (public Wi-Fi with a malicious profile, a compromised device, an intercepting proxy) and sits silently between app and server, reading and altering traffic.
- **Certificate pinning** is the defense: the app is told _exactly_ which server certificate or public key to trust and refuses any other, even if the system would accept it. Two flavors: pin the certificate itself, or pin its public key hash (more flexible across renewals).
- **The cost of pinning (a good trade-off lesson):** if you rotate your server certificate carelessly, you can **lock out your own users** until they update the app. Mitigations: pin the public key rather than the leaf certificate, include a backup pin, and plan rotations.
- **Also:** don't trust the client's own claims. Validate everything on the server.

### 2.5 The binary: raising the cost of reverse engineering (2 min)

**Obfuscation** renames and scrambles symbols in your compiled code, so `calculateUserDiscount` becomes something meaningless. In Flutter it's enabled at build time with the `--obfuscate` flag together with `--split-debug-info` (which also gives you symbol files so you can decode crash stack traces later; **keep those symbol files safe**, or your crash reports become unreadable).

**Honest framing:**

**SAY:** "Obfuscation doesn't make reverse engineering impossible. It makes it slower and more annoying. It's a lock on a bicycle: it won't stop a determined professional, but it convinces most people to walk to the next bike."

**Related ideas to name:**

- **Root/jailbreak detection**: signals that the device's protections may be broken. Easily bypassed by a determined attacker, but useful as one layer (and required for banking-grade apps).
- **App integrity attestation**: platform services (Google's Play Integrity API and Apple's App Attest/DeviceCheck) let your _server_ ask "is this really my genuine app, on a genuine device?" This shifts trust to the server, which is the right direction.
- **Runtime tamper detection**, and **native code protection** for very high-risk apps (ProGuard/R8 handle the Android native side).

**The deepest lesson of security:**

**SAY:** "There's no such thing as 'secure.' There's only 'expensive enough to attack that it isn't worth it.' Security is economics."

### 2.6 The server is the real authority (2 min)

**Never trust the client.** Every check inside the app ("is this user an admin?", "is this price valid?", "is this coupon still active?") can be bypassed by modifying the app or calling your API directly with a tool like a proxy or `curl`. **App checks exist for user experience. Server checks exist for security.** Re-validate everything on the server:

- **Authentication** (who are you?) and **authorization** (what are you allowed to do?): don't confuse them. A very common bug class is _broken object-level authorization_: user A changes an ID in the request and reads user B's data. The server must check ownership on every request.
- **Input validation** and **output encoding**: prevent injection attacks (SQL injection, NoSQL injection) on the server side.
- **Rate limiting** and **lockout** against brute-force attacks.
- **Backend rule misconfiguration.** If you use a backend-as-a-service (Firebase, Supabase, and similar), the _security rules_ are your authorization layer. "Test mode" open rules that are never tightened are a leading cause of real data breaches. Say this explicitly.

### 2.7 OWASP Mobile Top 10 and MASVS (2 min)

OWASP is a respected non-profit that publishes community-vetted security guidance. **VERIFY** the current edition, but the 2024 Mobile Top 10 themes are:

1. Improper credential usage
2. Inadequate supply chain security
3. Insecure authentication/authorization
4. Insufficient input/output validation
5. Insecure communication
6. Inadequate privacy controls
7. Insufficient binary protections
8. Security misconfiguration
9. Insecure data storage
10. Insufficient cryptography

**SAY:** "Notice that almost none of these are exotic hacking. They're _ordinary mistakes made by ordinary developers_. Which means they're preventable by ordinary discipline."

Also mention **MASVS** (Mobile Application Security Verification Standard) as a checklist of what "secure enough" means, and **MASTG** (the testing guide) for those who want to try attacking their own apps. Suggest that as a portfolio project: _"I security-tested my own app using the OWASP guide."_ That impresses interviewers.

**Supply chain (Top 10 #2) deserves a moment.** Every package you add is code you didn't write, running with your app's permissions. Practice: prefer well-maintained, popular packages; check the pub.dev score, publisher verification, and update history; keep dependencies updated; remove unused ones; don't add a package for something trivial.

**Privacy (Top 10 #6) deserves a moment.** Collect the minimum data you need, tell users what you collect, protect it, and delete it when asked. Privacy laws like GDPR (Europe) and similar regional regulations create real legal obligations, and store review processes check for privacy disclosures.

### 2.8 Discussion (1 min)

**ASK:** "If someone stole your user's phone, what could they access through your app? If someone downloaded and unpacked your app, what could they learn?"

### Anticipated student questions

**"Can Flutter apps be reverse engineered?"** Yes. Compiled Dart is harder to read than JavaScript or Java bytecode, but strings, assets, network endpoints, and logic can still be recovered by skilled people. Assume it can be analyzed.

**"Is Firebase secure?"** The platform is well-engineered. What's insecure is _how you configure it_. The service can only enforce the rules you write.

**"Do I need pinning for my class project?"** Probably not. Know what it is and when it's warranted (finance, health, high-value data). For most apps, correct HTTPS, good token handling, and server-side checks matter far more.

**"Where do I put the API key then?"** On your server. If a third-party service insists on a client-side key, restrict it (by platform identifier, quota, and scope) and monitor its usage.

**CUT (if late):** STRIDE, attestation, native-code protection; keep secure storage, secrets, "never trust the client." **EXPAND (if time):** walk through a threat model of a simple login-plus-profile app on the board, using the four boxes (device, app, network, server) and STRIDE as a prompt.

---

## Break (10 minutes)

Use the break to _not_ talk about the course. Tell students to think about one thing from Modules 1 and 2 they want to change in their own project. You'll come back to it in the closing.

---

## Module 3 (25 minutes): Networking, APIs, Data and Offline

**Spine line:** _Your app must keep working when the world doesn't._

### 3.0 The lie of localhost (2 min)

**SAY:** "When you developed, your API ran on your laptop or on fast Wi-Fi, and replied in milliseconds every single time. That was a lie. The real world has tunnels, elevators, crowded stadiums, throttled connections, overloaded servers, and users on a data cap."

**Latency, bandwidth, reliability: three different problems.** Latency is _delay_ (how long a round trip takes). Bandwidth is _capacity_ (how much data per second). Reliability is _whether it arrives at all_. A user in a moving train has all three problems at once.

**The mindset shift:**

> **Assume the network will fail. Design for that. Judge your app by how it behaves when things go wrong.**

The famous list of the **fallacies of distributed computing** begins with "the network is reliable" and "latency is zero." Mention it: it's a classic, and students will meet it again.

### 3.1 API fundamentals worth revisiting (4 min)

Students used APIs, but did they understand the contract? Cover these quickly.

**REST basics.**

- **Methods and their meaning**: `GET` (read, safe), `POST` (create), `PUT` (replace), `PATCH` (partial update), `DELETE` (remove).
- **Idempotency**: an operation is idempotent if doing it twice has the same effect as doing it once. `GET`, `PUT`, and `DELETE` should be idempotent; `POST` typically is not. **Why this matters on mobile:** flaky networks cause retries. Retrying a non-idempotent `POST` ("place order") can create _two orders_. Solution: **idempotency keys**, a unique ID the client sends so the server can recognize a duplicate.
- **Status codes as language**: `2xx` success; `3xx` redirect; `4xx` _the client did something wrong_ (`400` bad request, `401` unauthenticated, `403` forbidden, `404` not found, `409` conflict, `422` validation failed, `429` too many requests); `5xx` _the server failed_ (`500`, `502`, `503`, `504`). The app should treat `4xx` and `5xx` differently: retrying a `400` is pointless; retrying a `503` may work.
- **Headers that matter**: `Authorization`, `Content-Type`, `Accept`, `Cache-Control`, `ETag`, `Retry-After`.

**Other styles to name (so they aren't lost later):**

- **GraphQL**: the client asks for exactly the fields it wants, avoiding over-fetching. Trade-off: more server complexity, trickier caching.
- **gRPC**: fast, binary, strongly typed contracts. Common between services; less common directly from mobile apps.
- **WebSockets / Server-Sent Events**: persistent connections for real-time features (chat, live scores).
- **Push notifications** (Firebase Cloud Messaging and Apple's push service): the server reaching _out_ to the device when the app isn't open.

**Serialization.** Turning JSON into Dart objects and back. Hand-written parsing is error-prone; code generation (`json_serializable`, `freezed`) is the standard fix. The professional habit: **never trust the shape of a response.** Fields can be missing, null, or of the wrong type. Handle it, and _log it_ when it happens.

### 3.2 Handling failure like a grown-up (5 min)

**Different failures deserve different responses.** A generic "Something went wrong" is a small act of disrespect: it gives the user nothing to act on.

|Failure|What it means|Good response|
|---|---|---|
|No connectivity|Device is offline|Say so clearly; show cached content; offer retry; queue writes if you can|
|Timeout|Server slow or network poor|Retry (with backoff) once or twice, then explain|
|`401` Unauthorized|Session expired|Refresh the token silently; if that fails, return to login gracefully|
|`403` Forbidden|Not allowed|Explain permissions; don't retry|
|`404` Not found|Resource gone|Show a "not found" state; don't retry|
|`422` Validation|Bad input|Show _precisely_ what to fix, next to the field|
|`429` Too many requests|Rate limited|Wait per `Retry-After`; slow down|
|`5xx` Server error|Not the user's fault|Apologize; retry with backoff; suggest trying later|

**Timeouts.** Every request needs a timeout. The default of "wait forever" leaves users staring at a spinner. Distinguish connect timeout from receive timeout.

**Retry strategy.** Naive retry (hammer the server instantly) makes outages worse. Use **exponential backoff** (wait 1s, then 2s, then 4s...) with **jitter** (add randomness) so a thousand clients don't all retry at the exact same instant, causing a "thundering herd." Only retry _idempotent_ or _safely-keyed_ requests, and only for errors that might be transient (network failure, `502/503/504`, sometimes `429`).

**Circuit breaker (name it).** After repeated failures, stop calling the failing service for a while instead of piling on. Useful on servers and in advanced clients.

**Interceptors.** HTTP clients like Dio let you plug in interceptors: one place to add auth headers, log requests, handle `401`, and map errors. This centralizes cross-cutting concerns instead of scattering them.

**The token-refresh race condition (great advanced example).** Five requests fire at once; all get `401`; all try to refresh the token; four fail because the refresh token was already used. Solution: a single in-flight refresh that other requests wait on, then retry with the new token. Mention it as a real-world bug that bites almost every team once.

**Model errors as data.** Instead of throwing exceptions through five layers, many teams return a **Result** type (`Success(data)` or `Failure(error)`), or use a sealed hierarchy of error types (`NetworkError`, `AuthError`, `ServerError`, `ValidationError`). The UI then _must_ handle each case, and the compiler helps. Tie this to "impossible states" from Module 1.

**Connectivity checks are hints, not truth.** A "connected to Wi-Fi" flag doesn't mean the internet works (captive portals, dead routers). The only reliable test of whether a request will succeed is _making the request_. Treat connectivity plugins as hints to improve messaging, not as a gate.

### 3.3 Pagination: don't eat the whole cake (3 min)

**The scaling story.** In testing you had 20 products. In production there are 50,000. Loading all of them is slow, wastes data, blows memory, and hammers your server.

**Two main strategies:**

- **Offset/limit** (`?page=3&limit=20` or `?offset=40&limit=20`): simple and lets you jump to any page. **Weakness:** if items are inserted or deleted while the user scrolls, they may see duplicates or skip items; and large offsets get slow on big databases.
- **Cursor-based** (`?after=<last-item-id>&limit=20`): the server says "give me items after this marker." Stable under insertions and efficient at scale. **Trade-off:** you can't jump to "page 50" directly. It's the preferred approach for feeds and infinite scroll.

**On the UI side:** infinite scroll (load more as the user nears the end), with a loading footer, an error footer with retry, an "end of list" state, and pull-to-refresh. And use lazy list builders (`ListView.builder`) so off-screen items aren't built.

**SAY:** "Scalability is mostly about never doing more work than necessary."

### 3.4 Caching: the art of not asking twice (3 min)

**Why cache.** Speed (instant repeat views), cost (fewer server calls), battery, data plans, and resilience (something to show when offline).

**The layers of caching in a mobile app:**

1. **In-memory cache**: fastest, gone when the app closes.
2. **Disk/local database cache**: survives restarts. Common tools: SQLite via `sqflite` or the type-safe `drift`, key-value stores like Hive, and others. **VERIFY** the maintenance status of any local-database package before recommending it (this space changes).
3. **HTTP caching**: servers send `Cache-Control` (how long it's fresh) and `ETag` (a version fingerprint). The client sends `If-None-Match`; if nothing changed, the server replies `304 Not Modified` with no body, saving bandwidth.
4. **Image caching**: essential. Packages like `cached_network_image` keep downloaded images on disk.

**Strategies to name:**

- **Cache-aside / read-through**: check cache first; on miss, fetch and store.
- **TTL (time to live)**: cached data expires after a set time.
- **Stale-while-revalidate**: show cached data _immediately_, then refresh in the background and update the UI. This feels fast _and_ stays fresh. It's the sweet spot for many apps.

**The famous joke.** "There are only two hard things in computer science: cache invalidation and naming things." Cache too little and the app is slow; cache too much and it shows outdated or wrong data. **The key question for every piece of data: "How wrong is it allowed to be, and for how long?"** A news feed can be a minute stale. A bank balance cannot.

### 3.5 API versioning: the promise to old apps (2 min)

**The reality students don't know yet.** Once your app is published, **old versions live on people's phones for years.** Some users never update. If you change a response format tomorrow, every old app breaks, and you cannot force them to update in advance.

**Strategies:**

- **URL versioning**: `/v1/orders`, `/v2/orders`. Simple, visible. The most common.
- **Header versioning**: version in a request header. Cleaner URLs, less visible.
- **Additive changes**: adding new fields is usually safe; removing or renaming fields is _breaking_. Design clients to **ignore unknown fields**.
- **Minimum supported version + force update.** The server (or a remote config value) tells the app "your version is too old; please update." Plan this from the _first_ release, because you can't add it retroactively to versions already in the wild.
- **Deprecation policy**: announce, support both versions for a period, then retire.

**SAY:** "Versioning is a promise: I won't break you without warning."

### 3.6 Offline-first: a philosophy, not a feature (4 min)

**Most beginners treat offline as a bonus.** Offline-first flips the model.

> **The local database is the source of truth for the UI. The network is just a background process that synchronizes it.**

**How it works:**

1. The UI _always reads from local storage_, so it's always instant and always works.
2. Writes go to local storage first (**optimistic UI**: show success immediately).
3. A background sync process pushes local changes to the server and pulls remote changes down when a connection is available.
4. The UI updates automatically when local data changes (reactive queries).

**Why users love it:** no spinners for things they've already seen; the app works in the subway, on a plane, and with bad signal.

**The hard part: sync and conflicts.** What if the same item was edited on two devices while both were offline? Strategies:

- **Last-write-wins**: simplest; the newest timestamp wins. Can silently lose data. (Also, device clocks aren't trustworthy; prefer server timestamps or version counters.)
- **Merge by field**: combine non-conflicting edits.
- **Ask the user**: show both versions and let them choose.
- **CRDTs** (conflict-free replicated data types): mathematical structures that merge automatically without conflicts. Advanced; name them so students know the term.

**Also required:**

- A **write queue** (outbox) of pending operations that survives app restarts.
- **Idempotency keys** so retried operations don't duplicate.
- **Retry with backoff** for the queue.
- **Background execution** (WorkManager on Android, background tasks on iOS; the `workmanager` package wraps these). Note honestly that platforms restrict background work heavily to save battery.
- **Schema migrations** for the local database when your app updates. Forgetting this crashes updated apps for existing users.

**The trade-off (say it plainly):** offline-first adds serious complexity. Use it where it matters (notes, field-work apps, messaging, anything used in poor connectivity). For a simple content-browsing app, plain caching is enough.

**EXPAND:** discuss "optimistic UI with rollback": showing success immediately, then quietly reverting and notifying the user if the server rejects the change.

### 3.7 Discussion and anticipated questions (2 min)

**ASK:** "Pick one screen in your app. What happens right now if the internet drops mid-request? What will the user see? What _should_ they see?"

**"Should I always retry failed requests?"** No. Retry only errors that might be transient, only for safe (idempotent or keyed) requests, with a limit and with backoff. Retrying a `400` is pointless; retrying a payment without an idempotency key is dangerous.

**"REST or GraphQL?"** Depends on the team, the data shapes, and the tooling. REST is simpler and universal; GraphQL shines with complex, varied data needs. Don't pick either for fashion.

**"Which local database should I use?"** For relational data and queries, SQLite through `drift` or `sqflite` is a solid, boring, reliable choice. For simple key-value or small objects, lighter options exist. Check maintenance status and community activity before committing.

**CUT (if late):** GraphQL/gRPC aside, CRDTs, circuit breaker; keep the failure table, pagination, and offline-first idea. **EXPAND (if time):** walk one "add a note while offline" scenario end to end (local write → outbox → reconnect → sync → conflict → resolution).

---

## Module 4 (20 minutes): Quality: Testing, CI/CD, and Engineering Habits

**Spine line:** _Quality is what lets you change code without fear._

### 4.0 Open with a failure story (1 min)

The classic: a developer fixes one small bug on Friday afternoon. Monday morning, the login screen is broken, because the "small fix" touched shared code. Nobody noticed until users complained. Ask:

**ASK:** "How would you have known, before shipping, that the fix broke login?" (Answer: a test, or a very tedious manual check nobody remembers to do.)

### 4.1 Why we test (2 min)

**SAY:** "Testing is not about proving your code works. It's about being able to change your code without fear."

Without tests, every change is a gamble, and you find out the result from angry users. With tests, you have a **safety net**, and safety nets are what allow trapeze artists to attempt bold moves. Tests also serve as **living documentation**: a good test says "here is what this code is supposed to do."

**The economics.** A bug found while typing costs seconds. Found by a test costs minutes. Found by QA costs hours. Found by users costs reputation, reviews, and uninstalls. The cost of a bug rises roughly with every stage it survives.

### 4.2 The test pyramid (4 min)

**BOARD:** draw a triangle with three layers.

```
            /\
           /  \      Integration tests   (few, slow, realistic)
          /----\
         /      \    Widget tests        (some, fast, focused on UI)
        /--------\
       /          \  Unit tests          (many, tiny, very fast)
      /____________\
```

**Unit tests.** Test one function or class in isolation, with no UI and no network. "Does `calculateDiscount(100, 20)` return `80`?" They run in milliseconds, so you can have thousands. They're the foundation because they're cheap and precise: when one fails, you know exactly where to look.

**Widget tests.** Flutter's superpower. They render a widget (or screen) in a simulated environment, without a real device, and let you interact with it: tap a button, enter text, check what appears. Key vocabulary: `testWidgets`, `pump` (advance a frame), `pumpAndSettle` (wait for animations to finish), `find` (locate widgets), `expect` (assert). They're slower than unit tests but far faster than running the full app.

**Integration tests.** Run the _whole app_ on a real device or emulator, like a real user: launch, log in, add an item, check out. They catch problems the smaller tests can't see (plugins, navigation, real platform behavior), but they're slow and can be **flaky**, so reserve them for your most critical user journeys.

**Golden tests (a special kind of widget test).** Compare a widget's rendered image against a stored "golden" reference image, catching accidental visual changes. Useful, but brittle across platforms and fonts.

**Why a pyramid and not an ice-cream cone?** Teams that lean mostly on slow end-to-end tests get slow, flaky, expensive test suites. The pyramid says: _many cheap tests, few expensive ones._

### 4.3 What should you actually test? (3 min)

You can't test everything and shouldn't try. Ask:

**SAY:** "If this breaks, how bad is it, and how likely is it to break?"

**Test heavily:** money and calculations, authentication, data saving and loading, business rules, parsing of API responses, state transitions (loading → success/error), anything with tricky edge cases.

**Test lightly or not at all:** trivial getters, pure layout constants (is padding 16?), code you don't own (don't test the framework or packages).

**Test behavior, not implementation.** A good test says "when the user enters a wrong password, an error message appears," not "the method `_setErrorFlag` was called." Tests tied to implementation break every time you refactor, which destroys their purpose.

**Edge cases to always consider:** empty lists, null values, very long text, very large numbers, zero, negative numbers, special characters, slow networks, failed requests, and the first-ever launch with no data.

**Structure a test with Arrange-Act-Assert** (also called Given-When-Then): set up the situation, perform the action, verify the outcome. One test, one idea.

**Beautiful secret to share:**

**SAY:** "Code that's easy to test is usually well-designed code. Remember Module 1? Separated layers are testable layers. If something is painful to test, it's often a sign the design is tangled. Tests are a mirror for your architecture."

### 4.4 Test doubles (2 min)

To test a view model without a real server, you replace its dependencies with **test doubles**:

- **Stub**: returns canned answers ("always return this user").
- **Fake**: a simple working implementation (an in-memory repository).
- **Mock**: records how it was called, so you can verify interactions ("was `save` called once?"). Packages such as `mocktail` and `mockito` create these.
- **Spy**: wraps the real thing and records calls.

**The link to Module 1:** dependency injection is what makes this possible. If a class creates its own dependencies internally, you can't swap them. If it _receives_ them, you can hand it a fake. That's the payoff for all that architecture talk.

**PITFALL:** over-mocking. Tests that mock everything end up testing the mocks, not the behavior. Prefer fakes where reasonable.

**TDD (test-driven development), briefly.** Red (write a failing test), green (make it pass with the simplest code), refactor (clean up). It's not mandatory, but even trying it once changes how you think about design. Present it as a tool, not a religion.

**Coverage.** `flutter test --coverage` measures which lines your tests execute. It's a useful _flashlight_ for finding untested areas, but a terrible _goal_: 100% coverage with weak assertions proves nothing. Warn against chasing the number.

**Flaky tests.** Tests that sometimes pass and sometimes fail (timing, randomness, network dependence) erode trust until the team ignores failures. Fix or delete them. A test suite nobody trusts is worse than none.

### 4.5 CI/CD: the tireless, slightly annoying colleague (3 min)

**Continuous Integration (CI).** Every time code is pushed, an automated system builds the app, runs static analysis, and runs the tests. If anything fails, the change is blocked from merging. Tools you'll hear about: GitHub Actions, GitLab CI, Codemagic (Flutter-focused), Bitrise, and Fastlane for automating store-related tasks.

**Continuous Delivery/Deployment (CD).** Once checks pass, the system packages the app and (delivery) prepares it for release or (deployment) ships it automatically, for example to internal testers via TestFlight or Play's internal testing track.

**Why it matters, in human terms:**

**SAY:** "Humans forget, get tired, and say 'I'll test it later.' A machine doesn't. It's a tireless, slightly annoying colleague who says, 'No, this breaks the build, you can't merge.' That annoyance is exactly what protects a team."

**A minimal CI pipeline (describe in words):** checkout code → set up Flutter → get dependencies → format check → static analysis → run tests → build the app. Even that simple pipeline catches most careless mistakes.

**Static analysis and linting.** `flutter analyze` and the recommended lint rules (`flutter_lints`) catch bugs before they run: unused code, missing `await`, unsafe context use. `dart format` ends style arguments. Turn on warnings, and treat them seriously.

### 4.6 Engineering habits that separate professionals (3 min)

These are cheap and enormously valuable. Present them as a checklist.

**Version control discipline.**

- Commit small, focused changes with meaningful messages. "Fix login crash when email is empty" tells a story; "fix" and "asdf" do not.
- Use branches and pull requests, even when working alone; it builds the habit.
- A common message convention is _Conventional Commits_ (`feat:`, `fix:`, `docs:`). Optional, but popular.
- Branching styles: trunk-based development (short-lived branches, frequent merges) versus GitFlow (long-lived develop/release branches). Modern teams increasingly prefer the former for speed; mention both.

**Code review.** Having another human read your change catches bugs, spreads knowledge, and improves design. Give feedback about the _code_, not the person. When reviewed, don't defend, ask "what led you to see it that way?"

**Readability.** Names matter more than comments. `remainingRetryCount` beats `x`. Comments should explain _why_, not _what_. Small functions, shallow nesting, no magic numbers. **SAY:** "Code is read far more often than it's written. Write for the reader."

**Documentation.** A README with purpose, screenshots, setup steps, architecture overview, and known limitations. Plus ADRs (from Module 1) for key decisions.

**Semantic versioning.** `MAJOR.MINOR.PATCH`: bump MAJOR for breaking changes, MINOR for new features, PATCH for fixes. Flutter's `pubspec.yaml` uses `version: 1.2.0+5`, where the number after `+` is the build number.

**Managing technical debt consciously.** Keep a visible list. Decide deliberately when to pay it down. Leave the campsite cleaner than you found it (the _Boy Scout Rule_): small improvements every time you touch code.

**Refactoring** means improving structure without changing behavior, and it's only safe when you have tests. Another reason tests come first.

### 4.7 Discussion and anticipated questions (2 min)

**ASK:** "What's the one function in your project that, if it silently broke, would hurt the most? Is anything protecting it?"

**"Do companies really write tests?"** Good ones do, and interviewers increasingly ask about it. Even a modest test suite in your portfolio signals maturity.

**"How much time should testing take?"** Commonly a substantial fraction of development time, and it pays back in speed later. Start with the critical paths rather than aiming for full coverage.

**"Is TDD required?"** No. Use it when the logic is tricky and you can define the expected outcome clearly.

**CUT (if late):** golden tests, TDD, branching styles; keep the pyramid, "test what matters," and CI in plain words. **EXPAND (if time):** trace one bug from "user report" to "regression test added to CI" so students see the full loop.

---

## Module 5 (15 minutes): Performance

**Spine line:** _Performance is what makes an app pleasant._

### 5.0 Frame it correctly (1 min)

Cite the well-known warning by Donald Knuth: _"Premature optimization is the root of all evil."_ The full context is worth noting: he was warning against optimizing _without evidence_, not against caring about performance. The professional rule: **measure first, then fix what the measurements reveal.** Guessing wastes time and adds complexity.

**What users actually feel:** smoothness (no jank), speed (fast startup and screen loads), battery (no drain), size (download and storage), and responsiveness. Users don't think "the raster thread is behind." They think "this app is bad."

### 5.1 How Flutter draws a frame (3 min)

**The frame budget.** At 60 frames per second, each frame must be produced in about **16.7 milliseconds**. At 120 Hz screens, roughly **8.3 ms**. Miss the budget and the user sees a stutter, called **jank**.

**The pipeline, in words:** _build_ (widgets are created) → _layout_ (sizes and positions are computed) → _paint_ (drawing commands are recorded) → _composite and rasterize_ (the GPU draws pixels).

**Threads (worth knowing conceptually).** The **UI thread** runs your Dart code and builds the frame; the **raster thread** turns the frame into GPU work; plus platform and I/O threads. Jank can come from either the UI side (too much Dart work) or the raster side (too expensive to draw). DevTools shows both.

**Rendering engines.** Flutter has historically used Skia and has been moving to **Impeller**, a newer engine designed to avoid _shader compilation jank_ (stutter the first time an effect is drawn). **VERIFY** current defaults per platform on the official page, because rollout has changed over releases.

### 5.2 Measure before you fix (2 min)

**Never judge performance in debug mode.** Debug builds include extra checks and are _much_ slower. Test in **profile mode** on a **real device** (ideally a modest, older phone: if it's smooth there, it's smooth everywhere).

**Flutter DevTools** is the toolbox:

- **Performance view**: frame timeline; shows which frames missed budget and why.
- **CPU profiler**: which functions consume time.
- **Memory view**: allocations, growth over time, leak hunting.
- **Widget inspector**: the tree, and rebuild counts if enabled.
- **Network view**: request timing.

**SAY:** "The profiler doesn't care about your opinion. It shows what's actually slow. Often it isn't what you expected."

### 5.3 The big performance ideas (5 min)

**A. Rebuild less, and rebuild smaller.** Rebuilds are cheap _by design_, but careless ones cascade. Techniques:

- **Push state down**: keep state as close as possible to where it's used, so a changing counter doesn't rebuild the whole screen.
- **Split big widgets into smaller ones**, so only the changed part rebuilds.
- **Use `const` constructors** wherever possible; Flutter can skip rebuilding constant widgets entirely.
- **Use targeted listening**: `select` (Provider/Riverpod), `buildWhen` (Bloc), `ValueListenableBuilder`, `Consumer` scoped narrowly.
- **Keep `build()` pure and cheap.** No network calls, no heavy computation, no creating controllers inside `build`.
- **Use keys correctly** when list items reorder, so state stays with the right item.

**Analogy:** repainting one door versus repainting the whole house.

**B. Lists and scrolling.**

- Use lazy builders (`ListView.builder`, `GridView.builder`, slivers) so only visible items are created. Eagerly building a 10,000-item list in a `Column` is a classic disaster.
- Avoid `shrinkWrap: true` on long lists (it forces measuring everything).
- Providing `itemExtent` or a prototype item helps Flutter skip layout work.
- Keep item widgets cheap.

**C. Images (the number-one hidden cost).**

- Decoding a huge image and displaying it tiny wastes memory. Load appropriately sized images (`cacheWidth`/`cacheHeight`), or request resized versions from the server.
- Cache network images.
- Prefer modern formats (WebP) and compressed assets.
- Be careful with many large images in scrolling lists.

**D. Expensive visual effects.** Certain operations (`Opacity` on large subtrees, clipping, blur, shadows, `saveLayer` triggers) are costly. Prefer cheaper alternatives (animated opacity widgets, pre-rendered assets) and wrap frequently-repainting regions in `RepaintBoundary` to isolate repainting. Use judiciously, and only when profiling shows a need.

**E. Startup time.** Users judge you in the first two seconds. Don't do heavy initialization before the first frame; defer non-essential work (analytics setup, large reads) until after the UI appears; show something quickly.

**F. App size.** Smaller downloads mean higher install rates. Techniques: split by ABI, use app bundles, remove unused assets and packages, compress images, and consider deferred components for big optional features. Tree-shaking in release builds removes unused code and icons automatically.

**G. Battery and network.** Batch network calls, avoid polling when push or streams work, be careful with location and background work, and respect OS power restrictions.

### 5.4 The main thread, Dart's model, and Isolates (3 min)

**The essential concept, and a common misunderstanding.** Dart runs your code on a **single-threaded event loop** (per isolate). `async`/`await` does **not** create parallelism. It lets the single thread _wait without blocking_ (for I/O, timers, network) and do other things meanwhile. A `Future` that's waiting on a network call is fine. But **CPU-heavy work** (parsing a 20 MB JSON file, image processing, encryption, big sorts) inside a `Future` still _blocks the thread_ and freezes the UI.

**PITFALL:** "I used `async`, so it runs in the background." No. `async` means "I might wait." It doesn't mean "another core is helping."

**The event loop model (BOARD it):** there's a **microtask queue** (runs first, to completion) and an **event queue** (I/O, timers, taps). The loop drains microtasks, then takes one event, repeats. That's why a long synchronous function starves everything else.

**The solution: Isolates.** An isolate is a separate worker with its **own memory and own event loop**. Isolates _don't share memory_; they communicate by passing messages (which copy data, with some optimizations). This avoids the locks and data races of traditional threading.

**Analogy (the restaurant):** the main thread is the waiter, who must stay free to smile at tables and take orders. The heavy chopping happens in the kitchen (an isolate). The waiter never stops serving.

**In practice:** `Isolate.run()` runs a single function in a fresh isolate and returns its result (Dart 2.19 and later). `compute()` is Flutter's older convenience wrapper. Long-lived workers can use `Isolate.spawn` with ports. **Caveat:** isolates behave differently on the web; check what your target platforms support.

**When to use one:** the work takes a noticeable fraction of a frame (rule of thumb: more than a few milliseconds) _and_ is CPU-bound. Don't isolate trivial work: spawning has overhead.

### 5.5 Memory leaks (2 min)

**What a leak is.** Your app holds references to things it no longer needs, so the garbage collector can't reclaim them. Dart is garbage-collected, so leaks aren't "forgot to free," they're **"forgot to let go of the reference."** The app doesn't crash right away. It slowly grows heavier and slower until the OS kills it.

**Classic causes (list on board):**

- Not calling `dispose()` on `AnimationController`, `TextEditingController`, `ScrollController`, `FocusNode`, `PageController`.
- Not cancelling `StreamSubscription`s and `Timer`s.
- Listeners added to `ChangeNotifier`s and never removed.
- Closures that capture a `BuildContext` or a `State` and outlive the widget.
- Global singletons or caches that grow without bound.
- Calling `setState` after the widget is gone ("setState called after dispose"), a symptom of async work outliving its screen. Check `mounted`.

**The discipline:**

**SAY:** "Whatever you open, you must close. Whatever you subscribe to, you must unsubscribe from. Cleaning up in `dispose` isn't politeness; it's hygiene."

**How to find leaks:** watch the memory chart in DevTools while repeatedly opening and closing a screen. If memory ratchets upward and never drops, something isn't being released.

### 5.6 Discussion and anticipated questions (1 min)

**ASK:** "In your project, is there any place where you do heavy work directly in a button handler or in `build`? What would the user experience on an old phone?"

**"Is Flutter slow?"** Well-written Flutter apps are smooth. Slowness almost always comes from _how the app is written_ (rebuilds, images, blocking work), not from the framework itself.

**"Should I optimize now?"** Build clearly first, profile when something feels wrong, fix the measured bottleneck. But avoid obvious traps from day one: lazy lists, sized images, no heavy work in `build`.

**"When do I use an isolate?"** When CPU-bound work is long enough to threaten frame time, and it can be expressed as "input in, result out."

**CUT (if late):** RepaintBoundary/saveLayer details, app size, battery; keep frame budget, rebuild discipline, isolates, dispose. **EXPAND (if time):** walk through diagnosing "my list scrolls badly" as a detective story: measure, find the expensive frames, hypothesize (image decoding? rebuilds? layout?), test, confirm.

---

## Break (10 minutes)

---

## Module 6 (15 minutes): Shipping and Watching

**Spine line:** _A shipped app is a living thing, so keep it observable._

### 6.0 Frame it (1 min)

Many students believe the project ends when the code works. **Publishing is its own discipline, with its own surprises**, and launch day is the _start_ of the app's real life. After launch you're flying an aircraft; you need instruments.

### 6.1 Build and environment hygiene (2 min)

- **Debug vs profile vs release builds.** Release is what users get: optimized, no debug tools. **Always test the release build before shipping**; things sometimes behave differently (obfuscation, permissions, missing internet permission on Android, and so on).
- **Environments / flavors.** Separate _development_, _staging_, and _production_ (different API endpoints, different Firebase projects, different app IDs so they can coexist on a phone). Flutter supports flavors on Android and schemes on iOS. This prevents the horror story of testing against production data.
- **Configuration.** `--dart-define` for build-time values; remember (Module 2) that this is convenience, not secrecy.
- **Feature flags and remote config.** Turn features on or off, or change values, _without shipping a new version_. Powerful for staged features and emergency switches. Firebase Remote Config is a common tool.

### 6.2 Android release essentials (2 min)

- **App bundle (`.aab`)** is the format Google Play requires for new apps. Play then generates optimized APKs per device.
- **Signing.** Every release is signed with a cryptographic key that proves you are the author. With **Play App Signing** (the standard now), Google holds the _app signing key_, and you sign uploads with an **upload key**. If you lose the upload key, you can request a reset through Play. **Without Play App Signing (older apps, or other distribution), losing the key can mean you can never update that app.** Either way: back up your keystore securely, never commit it to Git, and don't share the passwords casually.
- **Identifiers and versions.** `applicationId` is permanent once published. `versionName` (human-readable) and `versionCode` (integer that must increase with each upload). In Flutter these come from `version: 1.2.0+5` in `pubspec.yaml`.
- **Play Console requirements.** Store listing (title, descriptions, screenshots, icon, feature graphic), a **privacy policy URL**, a **Data safety form** (declare what data you collect and why), content rating questionnaire, target audience, and compliance with the **target API level** rules that Google raises periodically. **VERIFY** current requirements: Google has introduced testing requirements for newly created personal developer accounts (a period of closed testing with a minimum number of testers before production access). Check the current numbers before telling students; they've changed.
- A one-time registration fee applies for a Google Play developer account. **VERIFY** current amount.
- **Testing tracks**: internal, closed, open, then production. Use them.
- **Staged rollout**: release to 1%, 5%, 20%, then 100%, watching crash rates at each step.

### 6.3 iOS release essentials (2 min)

- **Apple Developer Program**: an annual paid membership is required to publish on the App Store. **VERIFY** the current price and enrollment rules (individual vs organization; organizations need a D-U-N-S number).
- **Certificates, identifiers, and provisioning profiles**: Apple's signing system. Confusing at first; Xcode's automatic signing handles much of it. The idea is the same: cryptographic proof of who built the app and which devices or store it's for.
- **Bundle ID**, **version**, and **build number**. Every upload needs a new build number.
- **TestFlight**: Apple's beta testing system for internal and external testers. Use it.
- **App Store Connect**: where you manage listings, screenshots for required device sizes, pricing, and submission.
- **App Review.** Apple manually reviews apps against the App Review Guidelines. Common rejection reasons: crashes or bugs, incomplete features, misleading descriptions, missing privacy policy, requesting permissions without a clear purpose string, broken links, demo-account problems (reviewers need working credentials), and guideline issues around login options (for example, rules relating to _Sign in with Apple_ when you offer third-party sign-in; **VERIFY** current wording). Build review time into your schedule; delays and rejections are normal.
- **Privacy disclosures**: Apple's "privacy nutrition labels," and the App Tracking Transparency prompt if you track users across apps.
- You need a Mac (with Xcode) to build and upload iOS apps. Cloud CI services with Macs can substitute.

### 6.4 Privacy and legal responsibility (1 min)

**SAY:** "If your app handles user data at all, privacy isn't a formality. It's a legal and ethical responsibility."

- Write an honest **privacy policy** describing what you collect, why, how long you keep it, and who you share it with.
- Ask for **consent** where required, and let users **delete their data and account** (both stores require an in-app account deletion path for apps that create accounts; **VERIFY** current rules).
- Comply with the law where your users live. Europe's **GDPR**, and comparable regional data-protection laws, create obligations around consent, access, deletion, and breach notification.
- Extra care with **children's data**, **health data**, and **location**.
- Respect open-source **licenses** of packages you use.

### 6.5 Observability: giving yourself eyes (4 min)

Once real users have your app, **you're blind unless you install instruments.** Three pillars:

**1. Crash reporting.** Tools like **Firebase Crashlytics** and **Sentry** capture crashes and unhandled errors on real devices, including devices you never imagined, with stack traces, device model, OS version, and app version. Without them, users just uninstall and never tell you why. Wire up Flutter's global error handlers (`FlutterError.onError` and the platform dispatcher's error hook) so _uncaught_ errors are reported too. Remember to upload **symbol files** if you obfuscated (Module 2), or the traces are gibberish.

**Key metrics:** **crash-free users** and **crash-free sessions**. Both stores expose vitals (Android vitals in Play Console; crash and metrics data in App Store Connect) and can penalize poorly-behaving apps in visibility. Also watch **ANRs** (Android's "Application Not Responding").

**2. Analytics.** Understand what users actually _do_: which screens they visit, where they abandon flows (funnels), how many return (retention), daily and monthly active users. This is humbling. You'll discover the feature you spent three weeks on is barely touched and the small button you added in ten minutes is used constantly.

**SAY:** "Users are the only real judges of your design."

Be ethical: collect what you need, anonymize where possible, and disclose it (Section 6.4).

**3. Logging and monitoring.** Structured logs with levels (debug, info, warning, error); _never_ log secrets or personal data; server-side monitoring of API errors and latency; alerts when error rates spike.

**Also valuable:** performance monitoring in production (startup time, slow frames, slow network calls), **user feedback channels** (in-app feedback, store reviews; reply to reviews professionally), and **A/B testing** to compare designs with real data.

### 6.6 Releasing with care (2 min)

- **You can't recall an app from a phone.** Unlike a website, a bad mobile release stays on devices until users update. That's why **staged rollouts, feature flags, and force-update mechanisms** matter.
- **The rollout ritual:** internal testers → beta group → 1 to 5% of production → watch crash-free rate and key metrics for a day or two → expand gradually → 100%.
- **If something goes wrong:** _halt_ the rollout, use a remote flag to disable the broken feature if you have one, ship a hotfix, and communicate honestly.
- **Blameless postmortems.** After an incident, write down what happened, why, and what will change, focusing on _systems_, not on blaming individuals. This is the culture of mature teams.
- **Release notes and changelogs.** Tell users what changed, honestly.
- **Store presence (ASO).** Clear title, benefit-driven description, good screenshots, and a strong icon influence downloads more than most developers expect.
- **Plan for updates from day one.** Store updates are how you deliver fixes and features, and most successful apps ship regularly.

### 6.7 Discussion and anticipated questions (1 min)

**ASK:** "If your app crashed for 5% of users tomorrow, how would you even find out?"

**"Do I need to pay to publish?"** Both stores charge for developer accounts (one-time for Google Play, annual for Apple), and amounts change, so check the current fees.

**"How long does review take?"** Highly variable; often a day or two on Apple and quicker on Google, but new accounts, new apps, and sensitive categories can take longer. Never plan a launch date without slack.

**"Can I test on iOS without a Mac?"** Building and signing for iOS requires Apple's toolchain, so you need a Mac (physical or cloud-hosted).

**"What if I lose my keystore?"** Depends on whether you use Play App Signing (recoverable via an upload-key reset) or not (potentially fatal). Back it up in more than one secure place from day one.

**CUT (if late):** A/B testing, ASO, feature-flag details; keep signing, staged rollout, crash reporting, privacy. **EXPAND (if time):** tell a launch-day story (a crash affecting one device family, discovered within an hour thanks to crash reporting, fixed by halting the staged rollout).

---

## Module 7 (15 minutes): Careers, Portfolio, and Interviews

**Spine line:** _Keep yourself growing, because the tools will change three times in your career._

### 7.0 Frame it (1 min)

Students are in their final stretch. This module is where the course becomes personal. Speak from your own experience if you can: what you'd tell yourself at their age.

**SAY:** "A degree says you _studied_. Everyone in the applicant pile has one. What separates you is _evidence_: things you built, how you built them, and how you think about them."

### 7.1 Your portfolio is your voice (4 min)

**GitHub as your professional face.** Recruiters and hiring managers really do look. Guidelines:

- **A proper README for every project**: what it does, why it exists, screenshots or a short demo GIF, how to run it, the architecture in a paragraph, key decisions, and what you'd improve. **A project without a README is a book without a cover.**
- **Meaningful commit history.** It tells the story of how you work.
- **Pinned repositories**: choose your best three to five.
- **Fewer polished projects beat many abandoned ones.** Depth impresses more than volume. One well-documented, tested, published app is worth ten half-finished tutorials.
- **Never publish secrets.** Employers check, and bots check faster.
- **Show tests and CI.** A green build badge and a test folder signal maturity immediately.
- **Show your thinking**: a short "design decisions" or ADR section. It demonstrates judgment, which is the scarcest skill.

**A published app is a superpower.** A real store listing (even a small app) proves you can do the _whole_ journey: build, test, sign, submit, survive review, and maintain. Few graduates can say that.

**Beyond GitHub:**

- **CV/resume**: one page for juniors. Lead with projects and impact, not with a list of every tool. Use verbs and outcomes ("reduced startup time from X to Y") rather than duties.
- **LinkedIn**: a clear headline, a short summary, and projects linked.
- **Writing and talking**: a short blog post explaining something you learned, or a short demo video, sets you apart. Teaching forces understanding.
- **Open source**: even small contributions (fixing a typo in docs, a small bug fix) teach you to read other people's code and work in a review process.
- **Community**: local developer groups, Flutter communities, online forums, and hackathons. Opportunities usually arrive through people.

### 7.2 Where does Flutter lead? (4 min)

**SAY:** "Flutter is a fantastic starting point, but it's a _tool_, not a destiny."

**Road 1: Deeper into mobile.** Learn native Android (Kotlin, Jetpack Compose) or iOS (Swift, SwiftUI). Platform knowledge lets you write plugins, solve platform-specific problems, and understand what Flutter is abstracting. The person who can go native when Flutter runs out of road is rare and valuable. Also consider React Native or Kotlin Multiplatform to broaden your view.

**Road 2: Toward the backend.** Many students have already touched APIs and databases. Building the server side (data modeling, authentication, scalability, caching, queues, deployment, and monitoring) makes you a _complete_ engineer and reveals that the other half of the system is just as fascinating. Common stacks include Node.js, Python (Django/FastAPI), Java/Kotlin (Spring), Go, and .NET. Full-stack is a natural extension.

**Road 3: Toward data, AI, and machine learning.** Apps generate data, and data invites intelligence. Mobile plus ML (on-device models, recommendations, vision) is a growing area. It demands strong fundamentals: Python, statistics, linear algebra, and a lot of patience.

**Road 4: Toward security.** Anyone who found Module 2 thrilling should consider mobile security, application security, or penetration testing. There is real demand and real meaning in protecting people. Start with the OWASP guides, capture-the-flag (CTF) games, and legal practice labs.

**Road 5: Toward cloud and DevOps.** CI/CD, containers, infrastructure as code, and observability. Every product needs people who make shipping safe and repeatable.

**Road 6: Toward product, design, or leadership.** Understanding UX, product thinking, and team leadership is a valid direction for engineers who enjoy people and problems more than pure code.

**The key insight:**

**SAY:** "All of these roads share the same foundation: clear thinking, good architecture, testing habits, security awareness, and the ability to keep learning. The specific technology will change three times in your career. The _thinking_ won't."

**Choosing a direction (practical advice):**

- You don't have to choose forever. Choose something for the next 12 to 18 months and go _deep_; depth teaches you how to learn anything.
- Pick a direction by what you enjoy _when it's hard_, not only what pays well.
- Build a **T-shaped profile**: broad awareness of the whole system (the top of the T), plus real depth in one area (the stem).
- Try small experiments: a weekend project in a new area tells you more than a month of reading about it.

### 7.3 Common mistakes in graduation projects (2 min)

Patterns seen again and again (ask students to privately count how many apply to them):

1. **Building features instead of solving a problem.** A focused app that solves _one_ thing well beats twenty half-working features.
2. **Ignoring error and empty states.** The demo works; the real world doesn't.
3. **Leaving secrets in the code or the Git history.**
4. **No documentation.** Even you will forget how it works within two months.
5. **No tests at all.**
6. **Being unable to explain your own decisions.** "The tutorial did it" is a red flag. "I chose X over Y because..." is gold.
7. **Copy-pasting code you don't understand.** It works until it doesn't, and then you're helpless.
8. **Starting the report and the deployment at the last minute.**
9. **No plan for what data the app collects.** Privacy surprises at the defense are painful.
10. **Never showing the project to a real user.** Watch one real person try your app without helping them. It's the fastest way to learn.

### 7.4 Interviews: what they really test (3 min)

**Interviewers rarely want memorized definitions. They probe your reasoning.** Structure of a typical junior Flutter/mobile hiring process: a screening call, a technical conversation (fundamentals plus a look at your project), often a take-home task or live exercise, and a behavioral interview.

**Topics that reliably appear:**

- **Dart language**: null safety, `final` vs `const`, `Future` vs `Stream`, `async`/`await`, isolates, extension methods, mixins, sealed classes and pattern matching, generics, collections.
- **Flutter fundamentals**: widget types, `BuildContext`, lifecycle, keys, layout (Row/Column/Expanded/Flexible/Stack), navigation, forms, theming.
- **State management**: what you used, why, and the trade-offs.
- **Architecture**: how you structured your project and why.
- **Networking and data**: REST, error handling, pagination, caching, local storage.
- **Security basics**: token storage, HTTPS, secrets.
- **Testing**: what you test and how.
- **Performance**: rebuilds, lists, isolates.
- **Git and teamwork**.

**Behavioral questions (use the STAR method):** _Situation_, _Task_, _Action_, _Result_. Prepare three stories in advance: a hard bug you solved, a disagreement or mistake you learned from, and something you built that you're proud of.

**Practical interview tips:**

- Think out loud. Interviewers grade your reasoning more than your final answer.
- It's fine to say "I don't know, but here's how I'd find out."
- Ask questions at the end (about testing culture, code review, mentorship). It signals maturity.
- Be honest about your level. Overclaiming is easily exposed and costs trust.
- Prepare to walk through _your own project_ in detail: architecture, one hard bug, one thing you'd redo.

### 7.5 Interview question bank with model answers (reference; use as you like)

**Q: What's the difference between `StatelessWidget` and `StatefulWidget`?** A stateless widget has no mutable state of its own; its output depends only on its configuration and inherited data. A stateful widget owns a `State` object that persists across rebuilds and can trigger a rebuild via `setState`. Use stateless whenever possible; go stateful for local, ephemeral state like animations, controllers, or a form field's value, and for lifecycle work in `initState`/`dispose`.

**Q: What is `BuildContext`?** A handle to a widget's location in the tree (technically, its `Element`). It's used to look _up_ the tree for inherited data such as `Theme.of(context)` or a provider, and for navigation. Using a context after an async gap can be unsafe because the widget may be gone; check `mounted`.

**Q: How would you store a login token securely?** In platform secure storage (Keychain on iOS, Keystore-backed storage on Android) via a secure-storage package, not in shared preferences. Prefer short-lived access tokens with refresh tokens; make logout invalidate the session server-side; never log tokens.

**Q: What happens if the API call fails?** The failure is modeled explicitly (a result type or error states) and surfaced as a specific message: no connection, timeout, unauthorized, validation error, server error. I show cached data if available, allow retry, use backoff for transient errors, and handle `401` by refreshing the token once.

**Q: `Future` versus `Stream`?** A `Future` delivers a single value (or error) later; a `Stream` delivers a sequence of values over time (user events, socket messages, database changes). Both are used with async code; `await` for futures, `await for` or listening for streams.

**Q: Does `async`/`await` make code run in parallel?** No. It lets a single-threaded event loop wait without blocking. For true parallel CPU-bound work, you use isolates.

**Q: What is an isolate?** A separate worker with its own memory and event loop, communicating by message passing rather than shared memory. Used to keep heavy computation off the UI thread.

**Q: `const` versus `final`?** `final` is assigned once at runtime; `const` is a compile-time constant (and `const` widgets can be reused, allowing Flutter to skip rebuilding them).

**Q: Why are keys used?** To help Flutter match widgets to their existing elements/state when the widget list changes, especially for reordering or removing items in lists. Without keys, state can attach to the wrong item.

**Q: How do you avoid unnecessary rebuilds?** Push state down, split widgets, use `const`, listen narrowly (`select`, `buildWhen`, targeted builders), and keep `build` pure and cheap.

**Q: How did you structure your project and why?** (Your students should be able to answer this about their own project. A strong answer names layers, where state lives, how data flows, and _one trade-off they consciously made_.)

**Q: How did you test your app?** (Strong answer: unit tests for logic and parsing, widget tests for key screens, maybe one integration test for the main flow, plus CI running them; and honest about what isn't covered.)

**Q: Tell me about a bug that took you a long time to solve.** (This reveals more than any technical question. Strong answers: describe the symptom, how they narrowed it down, what the root cause was, what they learned, and what they changed to prevent recurrence.)

**Q: How do you handle app updates when the API changes?** Version the API, make changes additive when possible, tolerate unknown fields on the client, and use a minimum-supported-version mechanism with force update for breaking changes.

**Q: What's the difference between authentication and authorization?** Authentication proves who you are; authorization decides what you're allowed to do. Both are enforced on the server; the client only reflects them.

---

## Closing (5 minutes)

### Return to the three questions from the opening

Put the three questions back on the board:

- If a stranger tried to break your app, how long would it take them?
- If the internet dropped right now, what would your user see?
- If a new developer joined tomorrow, how long until they could safely change something?

**ASK:** "Now that you've seen the seven modules, has your answer changed? Which module gave you a concrete change you'll make this month?" Take a few answers. Also recall the thing they were asked to think about during the break.

### The send-off (say it in your own words)

Points to hit:

1. **They crossed a real line.** They can build a working app from nothing. Most people never do. Be proud.
2. **The profession is about responsibility over time**: making software clear enough for others to read, safe enough to trust, resilient enough to survive a bad network, and honest enough to admit when it breaks.
3. **Stay curious.** Tools change; curiosity is the only permanent skill.
4. **Read other people's code.** It's the fastest way to grow.
5. **Teach and explain.** If you can explain it, you understand it.
6. **Be kind to future you.** Every clear name and small function is a gift to the person who'll maintain your code, and that person is usually you.
7. **Build things you care about.** Passion survives the boring parts.
8. **Ask for help, and offer it.** Careers are built on people.

**Close with a concrete action.** Ask each student to write down _one_ change they'll make to their own project in the next week (for example: move the token to secure storage, add one unit test, add a README, add an error state). Small, specific commitments beat vague inspiration.

Thank them sincerely.

---

## Appendix A: Pacing Guide and Contingencies

**If you're running 15+ minutes behind** (cut in this order):

1. Riverpod/Bloc detail (keep the comparison table).
2. STRIDE, attestation, native-code protection.
3. GraphQL/gRPC/CRDT/circuit-breaker asides.
4. Golden tests, TDD, branching styles.
5. RepaintBoundary/saveLayer, app size, battery.
6. A/B testing, ASO.
7. Interview question bank (point them to the written notes).

**If you're running 15+ minutes ahead** (add in this order):

1. The end-to-end login-flow narration (Module 1).
2. A live threat-modeling exercise on the board (Module 2).
3. The offline "add a note while offline" scenario (Module 3).
4. The bug-to-regression-test story (Module 4).
5. The "my list scrolls badly" detective story (Module 5).
6. The launch-day story (Module 6).
7. A mock interview with one volunteer (Module 7).

**If the room is quiet:** ask _specific_ questions about _their_ projects, not general ones. "What does your app do when login fails?" gets more answers than "any questions?"

**If one student dominates:** thank them, and redirect: "Let's hear from someone who hasn't spoken yet."

**If someone challenges you and you don't know:** "Good question. I don't know for certain; here's how I'd find out." Then do exactly that. It teaches more than a confident guess.

**If your laptop or connection fails:** the notes are self-contained. Draw diagrams by hand if needed.

---

## Appendix B: Glossary

- **ADR**: Architecture Decision Record. A short document capturing an important design decision and its reasoning.
- **AOT**: Ahead-of-time compilation. Dart compiles to native code for release builds.
- **ANR**: Application Not Responding (Android).
- **Attack surface**: all the ways an attacker can interact with a system.
- **Backoff (exponential)**: waiting progressively longer between retries.
- **Bloc/Cubit**: stream-based state management pattern/library.
- **CI/CD**: continuous integration / continuous delivery or deployment.
- **Circuit breaker**: pattern that stops calling a failing dependency for a while.
- **Clean Architecture**: layered design with dependencies pointing inward.
- **Crash-free rate**: percentage of users or sessions without a crash.
- **CRDT**: conflict-free replicated data type; merges concurrent edits automatically.
- **Cursor pagination**: paging using a marker to the last-seen item.
- **DI**: dependency injection.
- **DTO**: data transfer object; mirrors an API response shape.
- **Element**: Flutter's persistent instance of a widget in the tree.
- **ETag**: a version fingerprint used for HTTP caching.
- **Fake / Mock / Stub / Spy**: kinds of test doubles.
- **Feature flag**: a switch to enable or disable functionality remotely.
- **Flaky test**: a test with inconsistent results.
- **Idempotent**: safe to perform multiple times with the same result.
- **Impeller**: Flutter's newer rendering engine.
- **Isolate**: Dart's unit of concurrency with its own memory.
- **Jank**: visible stutter from missed frames.
- **JWT**: JSON Web Token; signed, not encrypted.
- **Keychain / Keystore**: OS-provided secure storage on iOS / Android.
- **MASVS / MASTG**: OWASP mobile security verification standard / testing guide.
- **MVVM**: Model-View-ViewModel.
- **Obfuscation**: scrambling symbol names in compiled code.
- **Offline-first**: design where local data is the source of truth for the UI.
- **Optimistic UI**: showing success before the server confirms.
- **OWASP**: Open Worldwide Application Security Project.
- **Pinning (certificate)**: restricting trusted server identities to specific ones.
- **Repository**: class that hides where data comes from.
- **Semantic versioning**: MAJOR.MINOR.PATCH numbering.
- **Single source of truth**: each piece of data has exactly one owner.
- **SOLID**: five object-oriented design principles.
- **Stale-while-revalidate**: show cached data now, refresh in the background.
- **Technical debt**: accumulated cost of shortcuts.
- **TTL**: time to live for cached data.
- **Unidirectional data flow**: state flows down, events flow up.

---

## Appendix C: One-Page Cheat Sheet (for you to glance at while speaking)

|Module|Big idea|Signature line|The one thing to remember|
|---|---|---|---|
|Opening|"Works" is the entry ticket|Keep it alive|Three questions on the board|
|1. Architecture and state|Make change cheap|A layer is defined by what it refuses to know|Trade-offs; don't over-engineer|
|2. Security|Device belongs to the user|A client secret is a public key with a private name|Never trust the client|
|3. Network and data|Assume failure|Never do more work than necessary|Offline-first is a philosophy|
|4. Quality|Fearless change|Testable code is well-designed code|Test what matters|
|5. Performance|Measure first|`async` is not parallel|Dispose what you open|
|6. Shipping|Ship and observe|Users are the only real judges|Staged rollout; you can't recall an app|
|7. Career|Growth over tools|Technology changes; thinking doesn't|Portfolio = evidence|

---

## Appendix D: Student Self-Audit Checklist (hand out or display)

**Architecture**

- [ ] No HTTP calls or JSON parsing inside widgets
- [ ] One place for API base URL and configuration
- [ ] Clear place where each piece of state lives
- [ ] Loading, success, and error states modeled explicitly

**Security**

- [ ] Tokens in secure storage, not plain preferences
- [ ] No secret keys in the app or in Git history
- [ ] HTTPS only; no disabled certificate checks
- [ ] Server validates everything (auth, ownership, input)
- [ ] Backend security rules are not left in "test mode"
- [ ] No sensitive data in logs

**Networking**

- [ ] Timeouts on every request
- [ ] Specific, helpful error messages
- [ ] Pagination for large lists
- [ ] Sensible caching; something to show offline
- [ ] Plan for API changes (versioning, force update)

**Quality**

- [ ] Unit tests for the most critical logic
- [ ] At least one widget test
- [ ] Lints and analyzer clean
- [ ] Meaningful commits; README written

**Performance**

- [ ] Lazy lists; images sized properly
- [ ] Nothing heavy in `build()` or on the UI thread
- [ ] Controllers, subscriptions, and timers disposed
- [ ] Tested in profile/release mode on a real device

**Shipping**

- [ ] Release build tested
- [ ] Keystore/signing keys backed up (and not in Git)
- [ ] Privacy policy written; data collection disclosed
- [ ] Crash reporting connected
- [ ] Staged rollout planned

---

## Appendix E: Resources

**Official documentation (start here):**

- docs.flutter.dev: especially _App architecture_, _State management_, _Testing_, _Performance_, _Security_, and _Deployment_ sections
- dart.dev: language tour, _Effective Dart_, concurrency and isolates documentation
- pub.dev: package scores, publisher verification, and changelogs

**Security:**

- OWASP Mobile Application Security (Mobile Top 10, MASVS, MASTG)
- Official Android and Apple platform security documentation

**Store guidance:**

- Google Play Console Help (policies, Data safety, testing tracks)
- Apple App Store Review Guidelines and App Store Connect Help

**Architecture and craft:**

- _Clean Code_ and _Clean Architecture_ by Robert C. Martin
- _The Pragmatic Programmer_ by Hunt and Thomas
- _Refactoring_ by Martin Fowler
- _A Philosophy of Software Design_ by John Ousterhout
- _Designing Data-Intensive Applications_ by Martin Kleppmann (for the serious backend or sync-minded)

**Community and video:**

- The official Flutter YouTube channel (_Widget of the Week_, architecture and performance talks)
- Documentation and examples of whichever state management library you choose (Provider, Riverpod, Bloc)
- Flutter and Dart community forums and local developer meetups

**Tools to mention:** Flutter DevTools, Firebase Crashlytics, Sentry, GitHub Actions, Codemagic, Fastlane, Firebase Remote Config, and the OWASP testing guides.

_Because packages, store policies, and tool defaults change quickly, re-check every **VERIFY** item in these notes against current official sources before the session._

---

_End of instructor notes. Good luck, and enjoy the yapping._