from typing import Any, Dict, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Devices
from app.schemas.device import Device, DeviceBase, DeviceCreate, DeviceUpdate


class CRUDDevice(CRUDBase[Devices, DeviceCreate, DeviceUpdate]):
    def get_by_room_id(self, db: Session, *, room_id: int) -> Optional[Devices]:
        return db.query(Devices).filter(Devices.room_id == room_id).all()
    
    def get(self, db: Session, *, id: int) -> Optional[Devices]:
        return db.query(Devices).filter(Devices.id == id).first()

    def create(self, db: Session, *, obj_in: DeviceCreate) -> Devices:
        db_obj = Devices(
            room_id=obj_in.room_id,
            name=obj_in.name,
            category=obj_in.category
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, obj_in: DeviceCreate, id: int) -> Devices:
        db_device = self.get(db, id=id)
        db_device.room_id = obj_in.room_id
        db_device.name = obj_in.name
        db_device.category = obj_in.category
        db.commit()
        db.refresh(db_device)

        return db_device


device = CRUDDevice(Devices)