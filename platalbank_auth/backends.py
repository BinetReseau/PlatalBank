#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django_auth_ldap.backend import LDAPBackend

class FrankizLDAPBackend(LDAPBackend):
    def get_or_create_user(self, username, ldap_user):
        """
        This must return a (User, created) 2-tuple for the given LDAP user.
        username is the Django-friendly username of the user. ldap_user.dn is
        the user's DN and ldap_user.attrs contains all of their LDAP attributes.
        """
        model = self.get_user_model()

        def _get(attrname, fallback):
            try:
                return ldap_user.attrs[attrname][0]
            except (IndexError, AttributeError):
                return fallback

        last_name =  _get("sn", username).lower().title()
        first_name = _get("cn", username).lower().replace(last_name.lower(), "").strip().title() or username
        email = _get("mail", username+"@polytechnique.edu")
        phone = _get("brIP", "")
        room = _get("brIP", "")

        kwargs = {
            'username__iexact': username,
            'defaults': {
                "username": username.lower(),
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
                "phone_number": phone,
                "room": room
            }
        }

        return model.objects.update_or_create(**kwargs)
