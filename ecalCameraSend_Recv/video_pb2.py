# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='video.proto',
  package='pb.VideoStream',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bvideo.proto\x12\x0epb.VideoStream\"R\n\nVideoFrame\x12\x12\n\nframe_data\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"9\n\x0bVideoStream\x12*\n\x06\x66rames\x18\x01 \x03(\x0b\x32\x1a.pb.VideoStream.VideoFrameb\x06proto3'
)




_VIDEOFRAME = _descriptor.Descriptor(
  name='VideoFrame',
  full_name='pb.VideoStream.VideoFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_data', full_name='pb.VideoStream.VideoFrame.frame_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='pb.VideoStream.VideoFrame.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='pb.VideoStream.VideoFrame.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pb.VideoStream.VideoFrame.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=113,
)


_VIDEOSTREAM = _descriptor.Descriptor(
  name='VideoStream',
  full_name='pb.VideoStream.VideoStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='pb.VideoStream.VideoStream.frames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=172,
)

_VIDEOSTREAM.fields_by_name['frames'].message_type = _VIDEOFRAME
DESCRIPTOR.message_types_by_name['VideoFrame'] = _VIDEOFRAME
DESCRIPTOR.message_types_by_name['VideoStream'] = _VIDEOSTREAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoFrame = _reflection.GeneratedProtocolMessageType('VideoFrame', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOFRAME,
  '__module__' : 'video_pb2'
  # @@protoc_insertion_point(class_scope:pb.VideoStream.VideoFrame)
  })
_sym_db.RegisterMessage(VideoFrame)

VideoStream = _reflection.GeneratedProtocolMessageType('VideoStream', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOSTREAM,
  '__module__' : 'video_pb2'
  # @@protoc_insertion_point(class_scope:pb.VideoStream.VideoStream)
  })
_sym_db.RegisterMessage(VideoStream)


# @@protoc_insertion_point(module_scope)