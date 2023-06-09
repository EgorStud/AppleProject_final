"""empty message

Revision ID: 6aa7da3123b8
Revises: dafce01ef08b
Create Date: 2022-12-10 09:59:37.309951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa7da3123b8'
down_revision = 'dafce01ef08b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ava_file',
    sa.Column('ImgId', sa.Integer(), nullable=False),
    sa.Column('FileFormat', sa.String(length=10), nullable=False),
    sa.Column('FileBody', sa.Boolean(), nullable=True),
    sa.Column('UsLegId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ImgId')
    )
    op.create_table('backet',
    sa.Column('BackId', sa.Integer(), nullable=False),
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('ShopId', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('BackId')
    )
    op.create_table('comment',
    sa.Column('ComId', sa.Integer(), nullable=False),
    sa.Column('Text', sa.String(length=200), nullable=False),
    sa.Column('LikesCnt', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('UsPhId_p', sa.Integer(), nullable=True),
    sa.Column('ShopId_p', sa.Integer(), nullable=True),
    sa.Column('UsPhId_c', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('ComId')
    )
    op.create_table('delivery',
    sa.Column('DelId', sa.Integer(), nullable=False),
    sa.Column('MinDaysMKAD', sa.Integer(), nullable=True),
    sa.Column('MinDaysMO', sa.Integer(), nullable=True),
    sa.Column('MinDaysRF', sa.Integer(), nullable=True),
    sa.Column('CostMKAD', sa.Integer(), nullable=True),
    sa.Column('CostMO', sa.Integer(), nullable=True),
    sa.Column('CostRF', sa.Integer(), nullable=True),
    sa.Column('ShopId', sa.Integer(), nullable=False),
    sa.Column('UsLegId', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.Column('UpdateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('DelId')
    )
    op.create_table('favourite',
    sa.Column('FavId', sa.Integer(), nullable=False),
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('ShopId', sa.Integer(), nullable=True),
    sa.Column('ProductFlg', sa.Boolean(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('FavId')
    )
    op.create_table('leg_entity',
    sa.Column('UsLegId', sa.Integer(), nullable=False),
    sa.Column('NickName', sa.String(length=20), nullable=False),
    sa.Column('Password', sa.String(length=20), nullable=False),
    sa.Column('FIO', sa.String(length=40), nullable=False),
    sa.Column('CompanyName', sa.String(length=40), nullable=False),
    sa.Column('PhoneNumber', sa.String(length=20), nullable=False),
    sa.Column('ImgAvId', sa.Integer(), nullable=True),
    sa.Column('Email', sa.String(length=40), nullable=False),
    sa.Column('AdressFact1', sa.String(length=80), nullable=False),
    sa.Column('AdressFact2', sa.String(length=80), nullable=True),
    sa.Column('AdressFact3', sa.String(length=80), nullable=True),
    sa.Column('AdressLeg', sa.String(length=80), nullable=False),
    sa.Column('Agreement', sa.Boolean(), nullable=False),
    sa.Column('Acct_no', sa.String(length=34), nullable=False),
    sa.Column('Kor_no', sa.String(length=20), nullable=False),
    sa.Column('Bik', sa.String(length=10), nullable=False),
    sa.Column('Kpp', sa.String(length=10), nullable=False),
    sa.Column('Ogrn', sa.String(length=15), nullable=False),
    sa.Column('Inn', sa.String(length=12), nullable=False),
    sa.Column('ProviderFIO', sa.String(length=40), nullable=False),
    sa.Column('ProviderPhoneNumber', sa.String(length=20), nullable=True),
    sa.Column('ProviderEmail', sa.String(length=40), nullable=True),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.Column('UpdateDate', sa.Date(), nullable=False),
    sa.Column('UpdateUsId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('UsLegId')
    )
    op.create_table('map__get_item_way',
    sa.Column('GiwId', sa.Integer(), nullable=False),
    sa.Column('GiwExpl', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('GiwId')
    )
    op.create_table('map__status',
    sa.Column('StatusId', sa.Integer(), nullable=False),
    sa.Column('StatusExpl', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('StatusId')
    )
    op.create_table('map__topic',
    sa.Column('TopicId', sa.Integer(), nullable=False),
    sa.Column('TopicExpl', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('TopicId')
    )
    op.create_table('order',
    sa.Column('OrderId', sa.Integer(), nullable=False),
    sa.Column('CntItems', sa.Integer(), nullable=False),
    sa.Column('SumCost', sa.Integer(), nullable=False),
    sa.Column('DeliveryFlg', sa.Boolean(), nullable=False),
    sa.Column('DeliveryCost', sa.Integer(), nullable=True),
    sa.Column('DeliveryDate', sa.Date(), nullable=True),
    sa.Column('OrderStatusCode', sa.Integer(), nullable=False),
    sa.Column('GetItemWay', sa.Integer(), nullable=False),
    sa.Column('CheckLink', sa.String(length=60), nullable=False),
    sa.Column('OrderQRLink', sa.String(length=20), nullable=True),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('ShopId', sa.Integer(), nullable=False),
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('BackId', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.Column('UpdateStDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('OrderId')
    )
    op.create_table('order_arch',
    sa.Column('OrderId', sa.Integer(), nullable=False),
    sa.Column('CntItems', sa.Integer(), nullable=False),
    sa.Column('SumCost', sa.Integer(), nullable=False),
    sa.Column('DeliveryFlg', sa.Boolean(), nullable=False),
    sa.Column('DeliveryCost', sa.Integer(), nullable=True),
    sa.Column('DeliveryDate', sa.Date(), nullable=True),
    sa.Column('OrderStatusCode', sa.Integer(), nullable=False),
    sa.Column('GetItemWay', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('ShopId', sa.Integer(), nullable=False),
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('BackId', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.Column('UpdateStDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('OrderId')
    )
    op.create_table('phys_entity',
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('NickName', sa.String(length=20), nullable=False),
    sa.Column('Password', sa.String(length=20), nullable=False),
    sa.Column('FIO', sa.String(length=40), nullable=False),
    sa.Column('BirthDate', sa.Date(), nullable=False),
    sa.Column('Email', sa.String(length=40), nullable=False),
    sa.Column('PhoneNumber', sa.String(length=20), nullable=False),
    sa.Column('Agreement', sa.Boolean(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.Column('UpdateDate', sa.Date(), nullable=False),
    sa.Column('UpdateUsId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('UsPhId')
    )
    op.create_table('post',
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('ProductFlg', sa.Boolean(), nullable=False),
    sa.Column('DescrShort', sa.String(length=100), nullable=True),
    sa.Column('DescrFull', sa.String(length=400), nullable=True),
    sa.Column('LikesCnt', sa.Integer(), nullable=False),
    sa.Column('ProductName', sa.String(length=40), nullable=True),
    sa.Column('AvailibleFlg', sa.Boolean(), nullable=True),
    sa.Column('Cost', sa.Integer(), nullable=True),
    sa.Column('UsLegId', sa.Integer(), nullable=True),
    sa.Column('ShopId', sa.Integer(), nullable=True),
    sa.Column('UsPhId', sa.Integer(), nullable=True),
    sa.Column('Topic_1', sa.String(length=20), nullable=True),
    sa.Column('Topic_2', sa.String(length=20), nullable=True),
    sa.Column('Topic_3', sa.String(length=20), nullable=True),
    sa.Column('Topic_4', sa.String(length=20), nullable=True),
    sa.Column('Topic_5', sa.String(length=20), nullable=True),
    sa.Column('Topic_6', sa.String(length=20), nullable=True),
    sa.Column('Topic_7', sa.String(length=20), nullable=True),
    sa.Column('Topic_8', sa.String(length=20), nullable=True),
    sa.Column('Topic_9', sa.String(length=20), nullable=True),
    sa.Column('Topic_10', sa.String(length=20), nullable=True),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('PostId')
    )
    op.create_table('post_file',
    sa.Column('FileId', sa.Integer(), nullable=False),
    sa.Column('FileType', sa.String(length=10), nullable=False),
    sa.Column('FileFormat', sa.String(length=10), nullable=False),
    sa.Column('FileBody', sa.Boolean(), nullable=True),
    sa.Column('QRFlg', sa.Boolean(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('FileId')
    )
    op.create_table('shop',
    sa.Column('ShopId', sa.Integer(), nullable=False),
    sa.Column('ShopName', sa.String(length=40), nullable=False),
    sa.Column('DescrShort', sa.String(length=100), nullable=False),
    sa.Column('DescrFull', sa.String(length=400), nullable=True),
    sa.Column('UsLegId', sa.Integer(), nullable=False),
    sa.Column('Topic_1', sa.String(length=20), nullable=True),
    sa.Column('Topic_2', sa.String(length=20), nullable=True),
    sa.Column('Topic_3', sa.String(length=20), nullable=True),
    sa.Column('Topic_4', sa.String(length=20), nullable=True),
    sa.Column('Topic_5', sa.String(length=20), nullable=True),
    sa.Column('Topic_6', sa.String(length=20), nullable=True),
    sa.Column('Topic_7', sa.String(length=20), nullable=True),
    sa.Column('Topic_8', sa.String(length=20), nullable=True),
    sa.Column('Topic_9', sa.String(length=20), nullable=True),
    sa.Column('Topic_10', sa.String(length=20), nullable=True),
    sa.Column('CreateDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('ShopId')
    )
    op.create_table('subscribe',
    sa.Column('SubscrId', sa.Integer(), nullable=False),
    sa.Column('UsPhId', sa.Integer(), nullable=False),
    sa.Column('UsPhIdForSubscr', sa.Integer(), nullable=True),
    sa.Column('ShopId', sa.Integer(), nullable=True),
    sa.Column('SubscrDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('SubscrId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribe')
    op.drop_table('shop')
    op.drop_table('post_file')
    op.drop_table('post')
    op.drop_table('phys_entity')
    op.drop_table('order_arch')
    op.drop_table('order')
    op.drop_table('map__topic')
    op.drop_table('map__status')
    op.drop_table('map__get_item_way')
    op.drop_table('leg_entity')
    op.drop_table('favourite')
    op.drop_table('delivery')
    op.drop_table('comment')
    op.drop_table('backet')
    op.drop_table('ava_file')
    # ### end Alembic commands ###
