.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================
Membership group for active members
===================================

* Add user accounts of active members (=contacts with an active 
  subscription from `subscription_oca` module) automatically to a group
  of your choice.
* Also enables automatically:
  
  * Adding active members automatically to one or more eLearning courses
  * Assigning active members a specific pricelist

* When a member's subscription ends, the above access get revoked automatically

Configuration
=============
* Define which group (= `res.groups` record) should be treated as the membership 
  group by checking its "Is membership group" checkbox. Only one group may have
  this option.
* Assign a pricelist for your membership products. You can just use the default Odoo pricelist if
  you do not need to add e.g. discounted pricelists for members.
* Toggle the "Auto-add subscription members to this channel" checkbox in the eLearning
  courses of your choice. Also ensure "Show Course To" is set to "Course Attendees".
  
Usage
=====
* Start or end a member's subscription. Their group membership, pricelist and eLearning access
  gets adjusted automatically once `subscription_oca` module's 

Known issues / Roadmap
======================
* In next version upgrade, consider refactoring the "Auto-add subscription 
  members to this channel" feature to use the `enroll_groups_ids` core field instead.

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>
* Timo Kekäläinen <timo.kekalainen@futural.fi>
* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
