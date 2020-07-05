from __future__ import annotations

from typing import *


class Pipeline:
  @staticmethod
  def load(dll_path: str) -> Pipeline: ...
  def read(self, variable: Variable) -> object: ...
  def write(self, variable: Variable, value: object) -> None: ...
  def is_int(self, variable: Variable) -> bool: ...
  def is_float(self, variable: Variable) -> bool: ...
  def is_bit_flag(self, variable: Variable) -> bool: ...


class Variable:
  def __init__(self, name: str) -> None: ...
  @property
  def name(self) -> str: ...
  @property
  def frame(self) -> Optional[int]: ...
  @property
  def object(self) -> Optional[int]: ...
  @property
  def object_behavior(self) -> Optional[ObjectBehavior]: ...
  @property
  def surface(self) -> Optional[int]: ...
  def with_frame(self, frame: int) -> Variable: ...
  def without_frame(self) -> Variable: ...
  def with_object(self, object: int) -> Variable: ...
  def without_object(self) -> Variable: ...
  def with_object_behavior(self, behavior: ObjectBehavior) -> Variable: ...
  def without_object_behavior(self) -> Variable: ...
  def with_surface(self, surface: int) -> Variable: ...
  def without_surface(self) -> Variable: ...


class ObjectBehavior:
  pass


class Address:
  pass
