## Mezzanine_modeltranslation

This is a test project for the integration of [mezzanine][mez] and
[django-modeltranslation][modT].

Here is a `bash` script that, if run will set up the environement for
easy bug reproducibility: [https://gist.github.com/1626513](https://gist.github.com/1626513).

It is related to the bug described in [issue #106][106] in the mezzanine
repository (scroll down).

### In summary:

[django-modeltranslation][modT] can work with [Mezzanine][mez], but if
you only follow the instruction (translation.py with the fields and
_admin with the `pass` added to the class, unregistering/registering
in `urls.py`), when logged in users with `edit` rights try to view a
page with new content (newer than the last restart of the website) the
template will throw an error that the field you added translation to
does not exist.

The bug has been fixed by Anders Hoftee
([@macdhuibh](https://github.com/macdhuibh)). The workaround is to *not*
make the field uneditable in the `patch_translation_field`. (line #20
in `translation_admin.py`)



To reproduce the bug, in
`translation_admin.py` replace

    def patch_translation_field(self, db_field, field, **kwargs):

by

    pass

    def _______________patch_translation_field(self, db_field, field, **kwargs):


Instructions to reproduce the bug:

- login as an admin (admin:default)
- go to the page for adding blog entries
- create an entry (somewhat fill the title & content for the three languages)
- save
- click on "view entry"
- kaboom! The template crash when it tries to create the edit button for the title


A non logged in user would not see this error page (as he would not
see the "edit title" button/link).


[106]:(https://github.com/stephenmcd/mezzanine/issues/106)
[mez]:(https://github.com/stephenmcd/mezzanine/)
[modT]:(http://code.google.com/p/django-modeltranslation/)
