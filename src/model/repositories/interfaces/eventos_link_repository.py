from abc import ABC, abstractmethod
from src.model.entities.eventos_link import EventosLink


class EventosLinkRepositoryInterface(ABC):
  def insert(self,  event_id: int, subscriber_id: int) -> str: pass 
      
  def select_event_link(self, event_id: int, subscriber_id: int) -> EventosLink: pass