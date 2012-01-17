## Mezzanine_modeltranslation

This is a test project for the integration of [mezzanine][mez] and
[django-modeltranslation][modT].

Here is a `bash` script that, if run will set up the environement for
easy bug reproducibility: [https://gist.github.com/1626513](https://gist.github.com/1626513).

It is related to the bug described in [issue #106][106] in the mezzanine
repository (scroll down).

To reproduce the bug:

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
