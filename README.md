# Mezzanine integration with djang-modeltranslation

This is a test project for the integration of [Mezzanine][mez] and
[django-modeltranslation][modT].

It is related to the bug described in [issue #106][106] in the Mezzanine
repository (scroll down).

## Installation instructions

Here is a `bash` script that, when run, will create and set up a
virualenvironment for easy bug reproducibility:
[https://gist.github.com/1626513](https://gist.github.com/1626513). It
needs `python` and `virtualenv` (the remaining dependencies are
downloaded and installed with `pip` by the script).


## The Bug

[django-modeltranslation][modT] can work with [Mezzanine][mez], but if
you only follow the instruction (`translation.py` with the fields and
`_admin.py` with the `pass` added to the class, unregistering/registering
in `urls.py`), when logged in users with `edit` rights try to view a
page with new content (newer than the last restart of the website) the
template will throw an error that the field you added translation to
does not exist.

## The Fix

The bug has been fixed by Anders Hoftee
([@macdhuibh](https://github.com/macdhuibh)). The workaround is to
*not* let the django-modeltranslation package set the translated
fields `editable` to `False` in the `patch_translation_field`
method. This is achieved by copy-pasting the modeltranslation
`patch_translation_field` into the class that subclass the
`TranslationAdmin` in your project and modify it so that the field is
set to True (line #20 in `translation_admin.py`).

## The Bug reproduction

To reproduce the bug, in `translation_admin.py` de-activate the fix

    def patch_translation_field(self, db_field, field, **kwargs):

by replacing it with the original instruction from *django-modeltranslation*

    pass

    def _______________patch_translation_field(self, db_field, field, **kwargs):


Instructions to reproduce the bug:

- login as an admin (admin:default)
- go to the page for adding blog entries
- create an entry (somewhat fill the title & content for the three languages)
- save
- click on "view entry"
- kaboom! The template crash when it tries to create the edit button for the title.


A non logged in user would not see this error page (as he would not
see the "edit title" button/link).


[106]:(https://github.com/stephenmcd/mezzanine/issues/106)
[mez]:(https://github.com/stephenmcd/mezzanine/)
[modT]:(http://code.google.com/p/django-modeltranslation/)
