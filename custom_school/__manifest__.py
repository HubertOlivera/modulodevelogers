# -*- coding: utf-8 -*-
{
    'name': "Custom Schools",

    'summary': """
        Gestionar datos de una escuela, estudiantes y profesores.
    """,

    'description': """
        Agrega nuevos modelos para definir datos de una escuela, estudiantes y profesores.
    """,

    'author': "Hubert Jesus Olivera Ysla",
    'website': "https://www.linkedin.com/in/hubert-olivera-246447226/",
    # for the full list
    'category': 'Schools',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_student.xml',
        'views/school_subject.xml',
        'views/school_teacher.xml',
        'views/menuitem_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
