from django.contrib.auth.models import Group,Permission

def create_groups_permissions(sender,**kwargs):
    try:
        readers_group,created=Group.objects.get_or_create(name="Readers")
        editors_group,created=Group.objects.get_or_create(name="Editors")
        authors_group,created=Group.objects.get_or_create(name="Authors")

        #Creating Permissions
    
        readers_permissions=[
            Permission.objects.get(codename="view_post")
        ]
    
        authors_permissions=[
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post"),
            Permission.objects.get(codename="view_post")
        ]
    
         # creating own permissios to use get_or_create
        can_publish, created=Permission.objects.get_or_create(codename="can_publish",content_type_id=7,name="Can Publish Post")

        editors_permissions=[

            can_publish,
            Permission.objects.get(codename="view_post"),
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post")
        ]

        #Assign permission to groups

        readers_group.permissions.set(readers_permissions),
        authors_group.permissions.set(authors_permissions),
        editors_group.permissions.set(editors_permissions)

        print(" Groups and permissions created successfully")

    except Exception as e:
        print(f"An error occured{e}")


