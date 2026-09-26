# Python: From Fundamentals

> **Vault Hub:** [[MOC|🗺️ Vault MOC]] · [[Numpy/0.1 intro to Numpy|🔢 Numpy Track]] · [[python_fundamentals.py|▶️ Run Demos]] to Advanced Object-Oriented Programming

A complete, production-quality Python course and long-term reference for programmers who already know how to program.

---

## Who This Is For

You already understand programming concepts:

- variables, types, conditions, loops
- functions, scope, recursion
- basic data structures (arrays, lists, maps, sets)
- general OOP terminology (class, instance, inheritance, polymorphism)

What you want is to learn **Python itself** — deeply, precisely, and Pythonically — from core language fundamentals to a thorough mastery of Python's object model and advanced OOP.

This course does not waste time explaining what a loop *is*. It explains how Python's `for` iterates, why its `else` clause exists, where mutability bites you, and how its object model makes everything work.

---

## Learning Outcomes

By the end of this course you will:

- Understand Python's execution model: objects, references, identity, mutability, namespaces, and scope (LEGB)
- Use Python's built-in types and collections idiomatically and efficiently
- Write clean, PEP 8-compliant functions with correct parameter handling, closures, and decorators
- Master Python's import system, packages, and virtual environments
- Handle exceptions and I/O the Pythonic way (EAFP, context managers, `pathlib`)
- Be fluent in iteration: iterators, generators, `yield` / `yield from`, `itertools`, and context managers
- Understand decorators, introspection, functional tools, and CPython's memory/GC model
- **Deeply understand Python OOP**: classes, instances, `self`, attributes, methods, encapsulation, properties, descriptors, inheritance, MRO, mixins, polymorphism, duck typing, ABCs, Protocols
- Master advanced object model topics: magic methods, `__new__`/`__init__`, `__repr__`/`__str__`, equality/hashing, ordering, container/iterable/callable/context-manager protocols, attribute customization, operator overloading, metaclasses, dataclasses, `__slots__`, and practical class design
- Be able to design and critique Python class hierarchies using composition, SOLID, and Pythonic idioms — and keep this course as a long-term reference

---

## How the Course Is Structured

### Hierarchical Numbering

Every lesson is a single file. The number in the filename is the learning order.

```
XX.YY — topic
│   │
│   └── lesson number within the part
└────── part number (00–13)
```

Examples:

- `00.1` — first lesson of Part 00
- `01.5` — fifth lesson of Part 01
- `13.16` — sixteenth lesson of Part 13

Read numerically: `00.1 → 00.2 → … → 01.1 → 01.2 → … → 13.16`.  
Folders group parts; the numbers give the total order across folders.

> **Sorting note:** `01.10` comes after `01.9` numerically. If you list files lexically, `01.10` will sort between `01.1` and `01.2`; read it numerically.

### Folder Layout

```
python/
├── README.md                          ← you are here
├── 00_intro/                          ← Part 00 — Orientation
│   ├── 00.1_what-is-python.md
│   ├── 00.2_installation-and-interpreters.md
│   ├── 00.3_running-python.md
│   └── 00.4_pep8-tooling.md
├── 01_fundamentals/                   ← Part 01 — Core Language
│   ├── 01.1_objects-references-variables-identity.md
│   ├── 01.2_typing-dynamic-strong.md
│   ├── 01.3_numbers.md
│   ├── 01.4_booleans-truthiness.md
│   ├── 01.5_strings.md
│   ├── 01.6_bytes-bytearray.md
│   ├── 01.7_none-singletons.md
│   ├── 01.8_mutability-immutability.md
│   ├── 01.9_namespaces-scope-legb.md
│   └── 01.10_operators-expressions.md
├── 02_collections/                    ← Part 02 — Built-in Collections
│   ├── 02.1_lists.md
│   ├── 02.2_tuples.md
│   ├── 02.3_dictionaries.md
│   ├── 02.4_sets-frozensets.md
│   ├── 02.5_sequences-mappings.md
│   ├── 02.6_slicing-indexing.md
│   ├── 02.7_comprehensions.md
│   ├── 02.8_copying.md
│   └── 02.9_builtin-functions-for-collections.md
├── 03_control-flow/                   ← Part 03 — Control Flow
│   ├── 03.1_conditionals.md
│   ├── 03.2_loops.md
│   └── 03.3_pattern-matching.md
├── 04_functions/                      ← Part 04 — Functions
│   ├── 04.1_defining-functions.md
│   ├── 04.2_parameters.md
│   ├── 04.3_args-kwargs.md
│   ├── 04.4_positional-keyword-only.md
│   ├── 04.5_scope-closures-nonlocal.md
│   ├── 04.6_first-class-lambdas.md
│   ├── 04.7_decorators-intro.md
│   └── 04.8_annotations-type-hints.md
├── 05_modules-packages/                ← Part 05 — Code Organization
│   ├── 05.1_modules-import-system.md
│   ├── 05.2_packages.md
│   ├── 05.3_import-mechanics.md
│   ├── 05.4_venv-pip.md
│   └── 05.5_main-guard.md
├── 06_exceptions/                     ← Part 06 — Exceptions
│   ├── 06.1_hierarchy.md
│   ├── 06.2_try-except-finally.md
│   ├── 06.3_custom-exceptions.md
│   └── 06.4_chaining-context.md
├── 07_files-io/                       ← Part 07 — Files & I/O
│   ├── 07.1_open-text-binary.md
│   ├── 07.2_context-managers-with.md
│   ├── 07.3_pathlib.md
│   └── 07.4_serialization-json.md
├── 08_iteration/                      ← Part 08 — Iteration & Iteration Tools
│   ├── 08.1_iterable-iterator-protocol.md
│   ├── 08.2_generators.md
│   ├── 08.3_yield-delegation.md
│   ├── 08.4_itertools.md
│   ├── 08.5_context-managers-deep.md
│   └── 08.6_decorators-deep.md
├── 09_advanced/                       ← Part 09 — Advanced Language
│   ├── 09.1_introspection.md
│   ├── 09.2_functional-tools.md
│   └── 09.3_garbage-collection-memory.md
├── 10_oop-basics/                     ← Part 10 — OOP Fundamentals
│   ├── 10.1_classes-instances-self.md
│   ├── 10.2_instance-vs-class-attributes.md
│   ├── 10.3_methods-instance-class-static.md
│   ├── 10.4_encapsulation-naming.md
│   ├── 10.5_properties.md
│   └── 10.6_dict-slots-lookup.md
├── 11_oop-design/                     ← Part 11 — Object Relationships
│   ├── 11.1_composition-vs-inheritance.md
│   ├── 11.2_aggregation-association.md
│   └── 11.3_design-principles.md
├── 12_inheritance-polymorphism/       ← Part 12 — Inheritance & Polymorphism
│   ├── 12.1_single-inheritance-super.md
│   ├── 12.2_multiple-inheritance-mro.md
│   ├── 12.3_mixins.md
│   ├── 12.4_polymorphism-duck-typing.md
│   ├── 12.5_abstract-base-classes.md
│   └── 12.6_protocols-structural-typing.md
└── 13_advanced-oop/                   ← Part 13 — Advanced OOP & Object Model
    ├── 13.01_magic-methods-overview.md
    ├── 13.02_object-creation-new-init.md
    ├── 13.03_str-repr-format.md
    ├── 13.04_equality-hashing.md
    ├── 13.05_ordering.md
    ├── 13.06_container-protocol.md
    ├── 13.07_iterable-protocol.md
    ├── 13.08_callable.md
    ├── 13.09_context-manager-protocol.md
    ├── 13.10_descriptors.md
    ├── 13.11_attribute-access.md
    ├── 13.12_operator-overloading.md
    ├── 13.13_metaclasses.md
    ├── 13.14_dataclasses.md
    ├── 13.15_slots-performance.md
    └── 13.16_practical-design.md
```

**87 lessons + this index** — every lesson is a self-contained reference you can return to.

---

## Course Progression — The Full Map

### Part 00 — Intro & Tooling (4 lessons)
Ground orientation before syntax.

| Lesson | File | What You Learn |
|---|---|---|
| 00.1 | `00.1_what-is-python.md` | What Python is, history, implementations (CPython/PyPy), Zen, "batteries included," tradeoffs, everything-is-an-object, bytecode VM |
| 00.2 | `00.2_installation-and-interpreters.md` | Versions, installing (system/pkg/pyenv), `python` vs `python3` vs `py` (PEP 394/397), `pip`/`venv` |
| 00.3 | `00.3_running-python.md` | REPL, `_`, `python -i`, `python -m`, shebang, stdin, CLI flags, `PYTHONPATH`/`sys.path`, `help`/`dir` |
| 00.4 | `00.4_pep8-tooling.md` | PEP 8 (indent/line length/imports/naming), PEP 257 docstrings, `flake8`/`ruff`, `black`/`isort`, `mypy`, file template |

### Part 01 — Fundamentals (10 lessons)
The mental model everything else depends on.

| Lesson | File | What You Learn |
|---|---|---|
| 01.1 | `01.1_objects-references-variables-identity.md` | Objects, names vs references, `id`/`is` vs `==`, interning, aliasing, `del`, refcount |
| 01.2 | `01.2_typing-dynamic-strong.md` | Dynamic + strong + gradual typing, duck typing, `type` vs `isinstance`, `Any` |
| 01.3 | `01.3_numbers.md` | `int` arbitrary precision + `0x`/`0b`/`_`, `float` IEEE 754 pitfalls, `complex`/`Decimal`/`Fraction`, `math` |
| 01.4 | `01.4_booleans-truthiness.md` | `bool` is `int`, falsiness table, `__bool__`/`__len__`, `and`/`or` return value, `if x == 1 or 2` bug |
| 01.5 | `01.5_strings.md` | Immutable Unicode, quoting/raw/escapes, `encode`/`decode`, f-strings (`!s!r!a`, `:`, `=`), `.format`/`%`, methods |
| 01.6 | `01.6_bytes-bytearray.md` | `bytes` vs `str`, `bytearray`, `memoryview`, `hex`/`base64`, `b"".join` |
| 01.7 | `01.7_none-singletons.md` | `None`/`NoneType`, `is None`, `Ellipsis`, `NotImplemented`, sentinel `object()` pattern |
| 01.8 | `01.8_mutability-immutability.md` | Mutable vs immutable, hashing, mutable-default `[]` trap, `copy` vs `deepcopy`, `id` changes |
| 01.9 | `01.9_namespaces-scope-legb.md` | Namespaces as dicts, LEGB, `global`/`nonlocal`, comprehension scope, shadowing builtins |
| 01.10 | `01.10_operators-expressions.md` | Expression vs statement, chaining `1 < x < 10`, `is`/`in`, `and`/`or`, `:=` walrus, precedence, `__radd__` |

**Key takeaway:** After Part 01 you can predict what `a = b; b.append(1)` does for every type and explain why.

### Part 02 — Built-in Collections (9 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 02.1 | `02.1_lists.md` | Dynamic arrays, 11 list methods, `key=` + Timsort stability, stack vs `deque`, `* n` aliasing |
| 02.2 | `02.2_tuples.md` | Comma-defined, `(1,)` trap, packing/unpacking + `*`, `namedtuple`/`NamedTuple`, shallow immutability |
| 02.3 | `02.3_dictionaries.md` | Hash table, insertion-ordered 3.7+, views, `|`/`|=` merge 3.9, `__missing__`, `fromkeys` trap |
| 02.4 | `02.4_sets-frozensets.md` | Unordered unique, operator algebra `&| -^`, `frozenset` hashable, O(1) membership |
| 02.5 | `02.5_sequences-mappings.md` | `collections.abc` hierarchy, `Sequence`/`Mapping`, `range` lazy, `len`/`in`/iteration |
| 02.6 | `02.6_slicing-indexing.md` | Negative index, `start:stop:step` clipping, `slice` objects, `lst[a:b]=iter`, shallow copy |
| 02.7 | `02.7_comprehensions.md` | list/dict/set/genexp, `if` filtering, nesting, walrus, isolated scope, performance |
| 02.8 | `02.8_copying.md` | Alias vs shallow (`[:]`,`.copy()`,`copy.copy`) vs deep (`deepcopy`+`memo`), `__copy__`/`__deepcopy__` |
| 02.9 | `02.9_builtin-functions-for-collections.md` | `len`/`sum`/`min`/`max`+`key`, `sorted` vs `.sort`, `enumerate`/`zip(strict=True)`, `any`/`all`, `Counter`/`defaultdict`/`deque` |

### Part 03 — Control Flow (3 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 03.1 | `03.1_conditionals.md` | `if`/`elif`/`else` + indent, truthiness, `is` vs `==`, ternary, guard clauses, multi-line conditions |
| 03.2 | `03.2_loops.md` | `for`-each + `range`, `enumerate`/`zip`, `break`/`continue`/`else` (nobreak), `while`/`while True`, `itertools` |
| 03.3 | `03.3_pattern-matching.md` | `match`/`case` 3.10+, literal/class/sequence/mapping/`__match_args__`, guards, `|`/`as`/`_`, exhaustiveness |

### Part 04 — Functions (8 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 04.1 | `04.1_defining-functions.md` | `def` execution, implicit `None`, tuple returns, functions as objects, `__code__`/`__defaults__`, docstrings |
| 04.2 | `04.2_parameters.md` | Positional/keyword, evaluation order, defaults evaluated once, mutable-default trap, `None`-sentinel |
| 04.3 | `04.3_args-kwargs.md` | `*args`/`**kwargs` + `*`/`**` unpacking, `pos/defaults/*args/kwonly/**kwargs` order, forwarding |
| 04.4 | `04.4_positional-keyword-only.md` | `/` positional-only + `*` keyword-only (PEP 570/3102), `inspect.Parameter.kind`, API design |
| 04.5 | `04.5_scope-closures-nonlocal.md` | LEGB, `global`/`nonlocal`, cells/`__closure__`, late-binding loop/lambda fixes, factories |
| 04.6 | `04.6_first-class-lambdas.md` | First-class values, `lambda` limits, `map`/`filter`/`reduce` vs comps, `partial`, `operator` |
| 04.7 | `04.7_decorators-intro.md` | `@` desugaring, wrapping, `functools.wraps`, stacking `A(B(C(f)))`, factories `@deco(args)` |
| 04.8 | `04.8_annotations-type-hints.md` | `list[int]` modern vs `typing`, `Optional`/`Union` vs `|`, `TYPE_CHECKING`, `mypy`/`pyright` |

### Part 05 — Modules & Packages (5 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 05.1 | `05.1_modules-import-system.md` | `__name__`/`__file__`/`__dict__`, `import` vs `from` vs `as`, `sys.modules` singleton, circular imports |
| 05.2 | `05.2_packages.md` | Regular vs namespace (PEP 420), `__init__.py`, `__path__`, relative `.`/`..`, re-exports/PEP 562 lazy |
| 05.3 | `05.3_import-mechanics.md` | `sys.path`/`PYTHONPATH`/`.pth`, finders+loaders (`meta_path`/`ModuleSpec`), `importlib`, `reload`, PEP 8 ordering |
| 05.4 | `05.4_venv-pip.md` | `pyvenv.cfg`/`sys.prefix`, activation, `pip` specifiers, `freeze`/`requirements.txt`, `pyproject.toml` (PEP 621) |
| 05.5 | `05.5_main-guard.md` | `__name__` values, `if __name__ == "__main__"` + `main(argv)->int`, script vs `python -m`, `SystemExit` |

### Part 06 — Exceptions (4 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 06.1 | `06.1_hierarchy.md` | `BaseException` vs `Exception`, `KeyboardInterrupt`/`SystemExit`, hierarchy tree, `ExceptionGroup` 3.11, specificity |
| 06.2 | `06.2_try-except-finally.md` | `try`/`except`/`else`/`finally`, `as e` clearing, return-in-finally trap, `contextlib.suppress` |
| 06.3 | `06.3_custom-exceptions.md` | Subclassing, `super().__init__` + attributes, hierarchy design, naming, dataclass pitfalls, decision table |
| 06.4 | `06.4_chaining-context.md` | `__traceback__`, `__context__` vs `__cause__`, `raise from`/`from None`, `add_note` 3.11, `ExceptionGroup`/`except*` |

### Part 07 — Files & I/O (4 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 07.1 | `07.1_open-text-binary.md` | `r/w/a/x/+`, text vs binary, `encoding`/`errors`/`newline`/`buffering`, `read`/`seek`/`tell`, iteration |
| 07.2 | `07.2_context-managers-with.md` | Desugaring, `__enter__`/`__exit__`, suppression, multi `with`, `ExitStack`/`nullcontext`/`ContextDecorator` |
| 07.3 | `07.3_pathlib.md` | `PurePath` vs `Path`, `/` operator, `resolve`/`parts`/`parent`/`suffix`, `glob`/`rglob`/`iterdir`/`mkdir` |
| 07.4 | `07.4_serialization-json.md` | `json` 4 fns/params, tuple→list trap, custom `JSONEncoder`/`object_hook`, `pickle` RCE danger, `csv`/`configparser`/`TOML` |

### Part 08 — Iteration (6 lessons)
Python's iteration model — prerequisite for Pythonic OOP.

| Lesson | File | What You Learn |
|---|---|---|
| 08.1 | `08.1_iterable-iterator-protocol.md` | `__iter__`/`__next__`, `StopIteration`, `for` desugars to `iter`+`next`, `iter(sentinel)`, exhaustion |
| 08.2 | `08.2_generators.md` | Generator function vs object, suspension, `next`/`send`/`throw`/`close`, genexp vs list comp, lazy pipelines |
| 08.3 | `08.3_yield-delegation.md` | `yield from`, `StopIteration.value`, PEP 380 expansion, `send`/`throw` forwarding, `async` preview |
| 08.4 | `08.4_itertools.md` | `count`/`cycle`/`repeat`, `product`/`permutations`/`combinations`, `chain`/`islice`/`zip_longest`/`groupby` |
| 08.5 | `08.5_context-managers-deep.md` | `__enter__`/`__exit__(exc_type,val,tb)` + suppression, `@contextmanager`, `ContextDecorator`, `ExitStack` |
| 08.6 | `08.6_decorators-deep.md` | Parametrized factories, stacking order, `wraps`, `lru_cache` dissected, method binding `__get__`, class decorators |

### Part 09 — Advanced Language (3 lessons)
Bridge to deep OOP.

| Lesson | File | What You Learn |
|---|---|---|
| 09.1 | `09.1_introspection.md` | `dir` vs `__dict__` vs `getmembers`, `isinstance`/`issubclass`+MRO/ABCs, `getattr`/`hasattr` trap, `inspect` (`signature`/`getsource`) |
| 09.2 | `09.2_functional-tools.md` | `lambda` late-binding, `map`/`filter` (lazy) + `None`, `reduce` fold, `operator`, `partial`/`cache`/`cached_property`/`singledispatch` |
| 09.3 | `09.3_garbage-collection-memory.md` | `PyObject`/`ob_refcnt`/`ob_type`, `sys.getrefcount`+immortal 3.12, intern `[-5,256]`+`sys.intern`, cyclic GC generations, `weakref` family, `__del__` pitfalls, `tracemalloc` |

### Part 10 — OOP Fundamentals (6 lessons)
Python's object model, from the ground up.

| Lesson | File | What You Learn |
|---|---|---|
| 10.1 | `10.1_classes-instances-self.md` | Class as live `type` object, body execution, 3-arg `type`, `__new__`+`__init__`, explicit `self`, bound method `__get__` |
| 10.2 | `10.2_instance-vs-class-attributes.md` | Dual dicts, read vs write asymmetry, mutable class-attr pitfall, shadowing, `type(self)` vs `ClassName`, `ClassVar` |
| 10.3 | `10.3_methods-instance-class-static.md` | Descriptor binding, `@classmethod` alt constructors + `cls` polymorphism, `@staticmethod`, decision tree |
| 10.4 | `10.4_encapsulation-naming.md` | Consenting adults, `_private` vs `__mangled` vs `__dunder__` vs `name_`, `__all__`/`import *`, get/set anti-pattern |
| 10.5 | `10.5_properties.md` | `@property`/`@setter`/`@deleter`, `property()` call, data descriptor mechanics, `cached_property` vs `property` |
| 10.6 | `10.6_dict-slots-lookup.md` | `__dict__` vs `mappingproxy`, 5-step lookup + `__getattribute__` vs `__getattr__`, `__slots__` memory/restrictions/inheritance |

### Part 11 — Object Relationships & Design (3 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 11.1 | `11.1_composition-vs-inheritance.md` | `is-a` vs `has-a`/implemented-in-terms-of, fragile base class, manual/`__getattr__` delegation, mixin vs base vs composition table |
| 11.2 | `11.2_aggregation-association.md` | Association (use-a) vs aggregation (shared) vs composition (exclusive/dies), UML→Python, `copy` vs `deepcopy`, `weakref` suite |
| 11.3 | `11.3_design-principles.md` | Cohesion+LCOM, SRP/OCP/LSP/ISP/DIP mapped to Python, tell-don't-ask, value object vs entity, YAGNI/KISS, ticketing evolution |

### Part 12 — Inheritance & Polymorphism (6 lessons)

| Lesson | File | What You Learn |
|---|---|---|
| 12.1 | `12.1_single-inheritance-super.md` | Overriding, `super()` as MRO proxy, zero-arg lexical scope, cooperative `__init__`+` **kwargs`, 7 common mistakes |
| 12.2 | `12.2_multiple-inheritance-mro.md` | C3 linearization worked merge, diamond resolution, `__mro__`/`mro()`, cooperative chaining, `object.__init__` trap |
| 12.3 | `12.3_mixins.md` | 5-property mixin, `*Mixin` naming, mixin-first ordering, mixin vs base vs composition, collision handling |
| 12.4 | `12.4_polymorphism-duck-typing.md` | Nominal vs structural polymorphism, duck typing, EAFP vs LBYL+TOCTOU+benchmark, `isinstance` vs duck vs `Protocol`, `singledispatch` |
| 12.5 | `12.5_abstract-base-classes.md` | `ABC`/`@abstractmethod`, concrete template methods, `collections.abc`, `register()` virtual subclass, `__subclasshook__` |
| 12.6 | `12.6_protocols-structural-typing.md` | `Protocol`, `@runtime_checkable` shallow check, generic protocols+variance, `Protocol` vs `ABC` vs duck decision table |

### Part 13 — Advanced OOP & Object Model (16 lessons)
The deepest part — mastery.

| Lesson | File | What You Learn |
|---|---|---|
| 13.01 | `13.01_magic-methods-overview.md` | Dunder taxonomy table, syntax→method mapping, when each fires, `NotImplemented` vs `NotImplementedError` |
| 13.02 | `13.02_object-creation-new-init.md` | `__new__` (static, creates) vs `__init__` (init in place) vs metaclass `__call__`, singleton/interning/caching, `__slots__`+`__new__` |
| 13.03 | `13.03_str-repr-format.md` | `__repr__` unambiguous/`eval` roundtrip vs `__str__` readable fallback, `__format__` for f-strings, `!s`/`!r`/`!a` |
| 13.04 | `13.04_equality-hashing.md` | `__eq__`→`NotImplemented`, `__hash__` consistency + `None` for unhashable, default `id` hash, mutable hashing danger |
| 13.05 | `13.05_ordering.md` | `__lt__`/`__le__`/`__gt__`/`__ge__` + `NotImplemented` reflection, `total_ordering`, sorting uses `__lt__` |
| 13.06 | `13.06_container-protocol.md` | `__len__`/`__getitem__`/`__setitem__`/`__delitem__`/`__contains__`/`__missing__`/`__iter__`/`__reversed__`, slice objects |
| 13.07 | `13.07_iterable-protocol.md` | `__iter__`→iterator + `__next__`+`StopIteration`, iterable vs iterator, `__getitem__` legacy, `__iter__` as generator |
| 13.08 | `13.08_callable.md` | `__call__`, function vs stateful callable, strategy/decorator/counter, `operator` vs `__call__` |
| 13.09 | `13.09_context-manager-protocol.md` | `__enter__` return→`as`, `__exit__(exc_type,val,tb)` + `True` suppress, desugaring, `contextlib`, exception handling |
| 13.10 | `13.10_descriptors.md` | `__get__`/`__set__`/`__delete__` + `__set_name__`, data vs non-data, function binding `__get__`, validated/typed/lazy, `__slots__` |
| 13.11 | `13.11_attribute-access.md` | `__getattribute__` (all) vs `__getattr__` (fallback), `__setattr__`/`__delattr__`/`__dir__`, recursion trap + `object.__getattribute__` |
| 13.12 | `13.12_operator-overloading.md` | `__add__`/`__radd__`/`__iadd__`/reflected+augmented, `NotImplemented` propagation, unary, `Vector`/`Money` |
| 13.13 | `13.13_metaclasses.md` | `type` is class of classes, custom metaclass `__new__`/`__prepare__`/`__call__`, registry/validation/ORM, `__init_subclass__` simpler alternative |
| 13.14 | `13.14_dataclasses.md` | `@dataclass`, `field(default_factory=)`, `init`/`repr`/`eq`/`order`/`frozen`/`slots`/`kw_only`, `__post_init__` |
| 13.15 | `13.15_slots-performance.md` | `__slots__` fixed attrs, no `__dict__`, `__weakref__`, inheritance complexities, pickle, memory/speed benchmarks |
| 13.16 | `13.16_practical-design.md` | End-to-end domain (Banking/Inventory) evolving procedural→OOP, SOLID+composition+ABC/Protocol+dunder decisions+testing |

---

## Pedagogical Approach

### Audience Assumption
You already program. This course never explains *what* a loop is — it explains **how Python's loops work** and **why they are designed that way**.

### How vs Why

Every topic covers:

- **How** — precise mechanics, syntax, runtime behavior, what the interpreter does
- **Why** — design rationale, Pythonic idiom, tradeoffs vs other languages, when to use it

### Mental Models

Where Python is subtle (references, mutability, scope, descriptors, MRO, protocols), the course gives you a **mental model** you can simulate by hand: boxes-and-arrows for references, LEGB stack, descriptor priority ladder, C3 merge.

### Examples — Simple → Realistic → Advanced → Edge Cases

Every lesson follows the same progression:

1. **Simple** — minimal, shows syntax
2. **Realistic** — domain example (orders, users, bank accounts, datasets, configs) you could ship
3. **Advanced** — combines features, shows Pythonic composition
4. **Edge cases** — pitfalls, surprises, anti-patterns, and how to avoid them

All code is **PEP 8**, readable, and annotated with *what it demonstrates and why it works* — not just code dumps.

### Explicit Distinctions

When two concepts are commonly confused, the course states the distinction head-on:

- `is` vs `==`, `list` vs `tuple`, `__getattr__` vs `__getattribute__`, `__new__` vs `__init__`, `isinstance` vs duck vs `Protocol`, `__hash__` vs `__eq__`, composition vs inheritance, ABC vs Protocol, `bytes` vs `str`, EAFP vs LBYL, and dozens more.

### Pythonic vs Non-Pythonic

When there is an idiomatic way, the course explains *why* it is considered Pythonic (readability, correctness, performance) and contrasts it with the alternative.

---

## Conventions

- **Python version:** Modern Python **3.10+** (pattern matching `match`/`case`, `list[int]` generics, `X | Y` unions) with notes where behavior changed across 3.8/3.9/3.11/3.12.
- **Code style:** Strict **PEP 8** — `snake_case` functions, `PascalCase` classes, `UPPER_SNAKE` constants, 4-space indents, `black`/`isort` compatible.
- **Terminology:** Accurate CPython terminology — *name* (not variable in the C sense), *binding*, *object*, *reference*, *descriptor*, *MRO*, *protocol*, *dunder* — used consistently.
- **Examples:** Every `python` block is runnable. Copy, run, break, modify — that is the intended use.
- **Scope:** Core language → advanced OOP. **Not** web/Django, ML/data-science, DevOps. Those build on this foundation.

---

## How to Use This Course

### Linear Path (Recommended First Time)

Read in numeric order, `00.1` through `13.16`. Each lesson builds on previous ones; skipping ahead will leave gaps (e.g., `13.10 Descriptors` assumes `08.1 Iterable Protocol` and `10.3 Methods`).

Suggested pacing:

- **Week 1–2:** Parts 00–04 (language basics + functions) — do every exercise
- **Week 3:** Parts 05–07 (organization + exceptions + files) — build a small CLI tool
- **Week 4:** Parts 08–09 (iteration + advanced) — rewrite loops as generators/context managers
- **Week 5–6:** Parts 10–12 (OOP core) — model a domain with composition, mixins, ABC/Protocol
- **Week 7:** Part 13 (advanced object model) — revisit your domain and add dunders, descriptors, dataclasses, slots, metaclass/`__init_subclass__`

### Reference Path (After First Pass)

Jump via this index:

- Need truthiness? → `01.4`
- Need `__hash__` rules? → `13.04`
- Need MRO? → `12.2`
- Need `yield from`? → `08.3`
- Need descriptor vs property? → `13.10`

### Hands-On

For each lesson:

1. Read the explanation, then **run every code block** in a REPL or small script.
2. Break it — change one thing, predict the error, verify.
3. Do the "Common Mistakes" / "Edge Cases" sections as exercises.
4. At the end of each Part, build one small program that uses the Part's ideas.

---

## Recommended Tools

| Tool | Purpose | Lesson |
|---|---|---|
| `python` 3.10+ (`pyenv` or official installer) | Interpreter | 00.2–00.3 |
| `black` + `isort` / `ruff` | Auto-formatting + import sort | 00.4 |
| `flake8` / `ruff` | Linting | 00.4 |
| `mypy` / `pyright` | Static type checking | 04.8, 09.1, 12.6 |
| `venv` (`python -m venv`) + `pip` | Isolation + packages | 05.4 |
| `ipython` | Better REPL | 00.3 |
| `inspect`, `dis`, `gc`, `tracemalloc` | Introspection/memory — stdlib | 09.1, 09.3 |

---

## Further Reading (After This Course)

This course is self-contained for Python → advanced OOP. After it:

- **Python Language Reference & Data Model** — `docs.python.org/3/reference/datamodel.html` — the normative object model
- **PEP index** — `peps.python.org` — especially PEP 8, 20, 257, 484, 557, 560, 570, 585
- **"Fluent Python" (Luciano Ramalho)** — deep companion to this course's Part 13
- **typing docs** — `docs.python.org/3/library/typing.html` + `mypy` docs for gradual typing at scale
- **Standard library** — `collections.abc`, `functools`, `itertools`, `contextlib`, `pathlib`, `dataclasses`

---

## File Count & Verification

- **Parts:** 14 (00–13)
- **Lessons:** 87 files
- **Index:** this README

Verify:

```bash
find python -type f | wc -l   # 88 (87 lessons + README)
find python -type f | sort
python -m py_compile $(find python -name "*.md" -exec grep -l "```python" {} \;)  # no — markdown is not python; compile the code blocks manually if desired
```

All lessons are Markdown with ```python code blocks that are individually runnable. No external dependencies required to read.

---

## License & Contribution

This material is a teaching reference. Treat code examples as public-domain snippets. When you adapt patterns (e.g., descriptor, metaclass registry, dataclass), credit the Python docs and include tests.

If you extend the course, keep the numbering scheme and add new lessons as `13.17_…`, `13.18_…`, or a new Part `14_…` with the same `14.1_…` / `14.2_…` convention.

---

*Built for programmers who want to be genuinely proficient in Python — not just able to write a class, but able to explain its `__mro__`, its descriptor chain, and why `if obj:` does what it does.*

