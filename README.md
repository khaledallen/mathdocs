# mathdocs

A tool for building an understanding of mathematics that is based on the interconnectedness and dependencies of mathematical concepts and objects.
Inspired by code documentation tools that emphasize inheritence and dependencies over developing complexity.

## development

mathdocs uses django mostly.

run with `python3 manage.py runserver`

changes to the models require updating the migrations and database via `python3 manage.py makemigrations` and then `python3 manage.py migrate`.

### Todo
- [x] add \norm{G}{A} = \text{Norm}_G(A)
- [ ] Add subtheorems references to Theorem model
- [ ] enable creating/editing properties
- [ ] enable creating/editing axioms
- [ ] Add "Used in" to object models
- [ ] Add login to prevent random people for adding to the database
- [ ] Add steps to theorem proofs
- [ ] Add progressive reveal for theorem steps

- [x] Add examples to the models
- [x] enable LaTeX preview on creating/editing screens using LaTeXNotes
    - [x] object creating
    - [x] object editing
    - [x] theorem creating and edinting
- [x] enable editing objects
- [x] enable creating/editing theorems
- [x] Add "Hypothesis" to theorem models
- [x] Add "Conclusion" to theorem models