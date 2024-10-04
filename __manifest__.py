# -*- coding: utf-8 -*-
{
    'name': "Animal Management",
    'summary': """My animal""",
    'description': """Managing animal information""",
    'author': "NQT",
    'website': "https://citgroup.vn/phan-mem-quan-ly-cua-hang-thu-cung.html",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/pet.xml',
        'views/pet_profiles.xml',
        'views/pet_caretaker.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}