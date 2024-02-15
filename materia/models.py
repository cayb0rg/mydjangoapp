# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asset(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_collation='utf8mb3_bin')
    type = models.CharField(max_length=10)
    created_at = models.IntegerField()
    title = models.CharField(max_length=300)
    file_size = models.IntegerField()
    deleted_at = models.IntegerField()
    is_deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'asset'


class AssetData(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_collation='utf8mb3_bin')  # The composite primary key (id, size) found, that is not supported. The first column is selected.
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    bytes = models.IntegerField()
    hash = models.CharField(max_length=255)
    created_at = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'asset_data'
        unique_together = (('id', 'size'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DateRange(models.Model):
    id = models.BigAutoField(primary_key=True)
    semester = models.CharField(max_length=255)
    year = models.IntegerField()
    start_at = models.IntegerField()
    end_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_range'
        unique_together = (('semester', 'year', 'start_at', 'end_at'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Log(models.Model):
    id = models.BigAutoField(primary_key=True)
    play_id = models.CharField(max_length=100, db_collation='utf8mb3_bin')
    type = models.CharField(max_length=26, blank=True, null=True)
    item_id = models.CharField(max_length=255)
    text = models.TextField()
    value = models.CharField(max_length=255)
    created_at = models.IntegerField()
    game_time = models.IntegerField()
    visible = models.CharField(max_length=1)
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'log'


class LogActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=255)
    created_at = models.IntegerField()
    item_id = models.CharField(max_length=100, db_collation='utf8mb3_bin')
    value_1 = models.CharField(max_length=255, blank=True, null=True)
    value_2 = models.CharField(max_length=255, blank=True, null=True)
    value_3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_activity'


class LogPlay(models.Model):
    id = models.CharField(primary_key=True, max_length=100, db_collation='utf8mb3_bin')
    inst_id = models.CharField(max_length=10, db_collation='utf8mb3_bin')
    is_valid = models.CharField(max_length=1)
    created_at = models.IntegerField()
    user_id = models.PositiveBigIntegerField()
    ip = models.CharField(max_length=20)
    is_complete = models.CharField(max_length=1)
    score = models.DecimalField(max_digits=52, decimal_places=2)
    score_possible = models.IntegerField()
    percent = models.FloatField()
    elapsed = models.IntegerField()
    qset_id = models.IntegerField()
    environment_data = models.TextField()
    auth = models.CharField(max_length=100)
    referrer_url = models.CharField(max_length=255)
    context_id = models.CharField(max_length=255)
    semester = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'log_play'


class LogStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    inst_id = models.CharField(max_length=10, db_collation='utf8mb3_bin')
    play_id = models.CharField(max_length=100, db_collation='utf8mb3_bin')
    user_id = models.PositiveBigIntegerField()
    created_at = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'log_storage'


class Lti(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.CharField(max_length=255, db_collation='utf8mb3_bin')
    resource_link = models.CharField(max_length=255)
    consumer = models.CharField(max_length=255)
    consumer_guid = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    context_id = models.CharField(max_length=255, blank=True, null=True)
    context_title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lti'


class MapAssetToObject(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.CharField(max_length=255, db_collation='utf8mb3_bin')
    object_type = models.IntegerField()
    asset_id = models.CharField(max_length=10, db_collation='utf8mb3_bin')

    class Meta:
        managed = False
        db_table = 'map_asset_to_object'
        unique_together = (('object_id', 'object_type', 'asset_id'),)


class MapQuestionToQset(models.Model):
    id = models.BigAutoField(primary_key=True)
    qset_id = models.PositiveBigIntegerField()
    question_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'map_question_to_qset'


class Migration(models.Model):
    type = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    migration = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'migration'


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_id = models.PositiveBigIntegerField()
    to_id = models.PositiveBigIntegerField()
    item_type = models.IntegerField()
    item_id = models.CharField(max_length=100, db_collation='utf8mb3_bin')
    is_email_sent = models.CharField(max_length=1)
    created_at = models.IntegerField()
    is_read = models.CharField(max_length=1)
    subject = models.CharField(max_length=511)
    avatar = models.CharField(max_length=511)
    updated_at = models.IntegerField()
    action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notification'


class PermObjectToUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.CharField(max_length=10, db_collation='utf8mb3_bin')
    user_id = models.PositiveBigIntegerField()
    perm = models.IntegerField()
    object_type = models.IntegerField()
    expires_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perm_object_to_user'
        unique_together = (('object_id', 'user_id', 'perm', 'object_type'),)


class PermRoleToPerm(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.PositiveBigIntegerField()
    perm = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'perm_role_to_perm'
        unique_together = (('role_id', 'perm'),)


class PermRoleToUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    role_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'perm_role_to_user'
        unique_together = (('user_id', 'role_id'),)


class PermRoleToUserBackup(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    role_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'perm_role_to_user_backup'


class PollsChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    hash = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'question'


class Sessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    previous_id = models.CharField(unique=True, max_length=40)
    user_agent = models.TextField()
    ip_hash = models.CharField(max_length=32)
    created = models.PositiveIntegerField()
    updated = models.PositiveIntegerField()
    payload = models.TextField()

    class Meta:
        managed = False
        db_table = 'sessions'


class UserExtraAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    inst_id = models.CharField(max_length=100, db_collation='utf8mb3_bin')
    user_id = models.PositiveBigIntegerField()
    created_at = models.IntegerField()
    extra_attempts = models.IntegerField()
    context_id = models.CharField(max_length=255)
    semester = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_extra_attempts'


class UserMeta(models.Model):
    user_id = models.PositiveBigIntegerField(primary_key=True)  # The composite primary key (user_id, meta) found, that is not supported. The first column is selected.
    meta = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_meta'
        unique_together = (('user_id', 'meta'),)


class UserRole(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_role'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    last_login = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()
    password = models.CharField(max_length=255)
    login_hash = models.CharField(max_length=255)
    profile_fields = models.TextField()
    updated_at = models.PositiveIntegerField()
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Widget(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.PositiveIntegerField()
    flash_version = models.PositiveIntegerField()
    height = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    is_scalable = models.CharField(max_length=1)
    score_module = models.CharField(max_length=100)
    score_type = models.CharField(max_length=13)
    is_qset_encrypted = models.CharField(max_length=1)
    is_answer_encrypted = models.CharField(max_length=1)
    is_storage_enabled = models.CharField(max_length=1)
    is_editable = models.CharField(max_length=1)
    is_playable = models.CharField(max_length=1)
    is_scorable = models.CharField(max_length=1)
    in_catalog = models.CharField(max_length=1)
    creator = models.CharField(max_length=255)
    clean_name = models.CharField(max_length=255)
    player = models.CharField(max_length=255)
    api_version = models.IntegerField()
    package_hash = models.CharField(max_length=32, db_collation='utf8mb3_bin')
    score_screen = models.CharField(max_length=255)
    restrict_publish = models.CharField(max_length=1)
    creator_guide = models.CharField(max_length=255)
    player_guide = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'widget'


class WidgetInstance(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_collation='utf8mb3_bin')
    widget_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    created_at = models.IntegerField()
    name = models.CharField(max_length=100)
    is_draft = models.CharField(max_length=1)
    height = models.IntegerField()
    width = models.IntegerField()
    open_at = models.IntegerField()
    close_at = models.IntegerField()
    attempts = models.IntegerField()
    is_deleted = models.CharField(max_length=1)
    guest_access = models.CharField(max_length=1)
    is_student_made = models.CharField(max_length=1)
    updated_at = models.IntegerField()
    embedded_only = models.CharField(max_length=1)
    published_by = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget_instance'


class WidgetMetadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    widget_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'widget_metadata'


class WidgetQset(models.Model):
    id = models.BigAutoField(primary_key=True)
    inst_id = models.CharField(max_length=10, db_collation='utf8mb3_bin')
    created_at = models.IntegerField()
    data = models.TextField()
    version = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget_qset'
