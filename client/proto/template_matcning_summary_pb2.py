# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/template-matcning-summary.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/template-matcning-summary.proto',
  package='templatematchingSummary',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%proto/template-matcning-summary.proto\x12\x17templatematchingSummary\x1a\x1cgoogle/protobuf/struct.proto\"@\n\x0eSummaryRequest\x12.\n\rmatching_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"@\n\x0fSummaryResponse\x12-\n\x0csummary_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\x86\x01\n\x17TemplateMatchingSummary\x12k\n\x14get_matching_summary\x12\'.templatematchingSummary.SummaryRequest\x1a(.templatematchingSummary.SummaryResponse\"\x00\x42\x02P\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SUMMARYREQUEST = _descriptor.Descriptor(
  name='SummaryRequest',
  full_name='templatematchingSummary.SummaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matching_data', full_name='templatematchingSummary.SummaryRequest.matching_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=96,
  serialized_end=160,
)


_SUMMARYRESPONSE = _descriptor.Descriptor(
  name='SummaryResponse',
  full_name='templatematchingSummary.SummaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary_data', full_name='templatematchingSummary.SummaryResponse.summary_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=162,
  serialized_end=226,
)

_SUMMARYREQUEST.fields_by_name['matching_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SUMMARYRESPONSE.fields_by_name['summary_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['SummaryRequest'] = _SUMMARYREQUEST
DESCRIPTOR.message_types_by_name['SummaryResponse'] = _SUMMARYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SummaryRequest = _reflection.GeneratedProtocolMessageType('SummaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUMMARYREQUEST,
  '__module__' : 'proto.template_matcning_summary_pb2'
  # @@protoc_insertion_point(class_scope:templatematchingSummary.SummaryRequest)
  })
_sym_db.RegisterMessage(SummaryRequest)

SummaryResponse = _reflection.GeneratedProtocolMessageType('SummaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUMMARYRESPONSE,
  '__module__' : 'proto.template_matcning_summary_pb2'
  # @@protoc_insertion_point(class_scope:templatematchingSummary.SummaryResponse)
  })
_sym_db.RegisterMessage(SummaryResponse)


DESCRIPTOR._options = None

_TEMPLATEMATCHINGSUMMARY = _descriptor.ServiceDescriptor(
  name='TemplateMatchingSummary',
  full_name='templatematchingSummary.TemplateMatchingSummary',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=229,
  serialized_end=363,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_matching_summary',
    full_name='templatematchingSummary.TemplateMatchingSummary.get_matching_summary',
    index=0,
    containing_service=None,
    input_type=_SUMMARYREQUEST,
    output_type=_SUMMARYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEMPLATEMATCHINGSUMMARY)

DESCRIPTOR.services_by_name['TemplateMatchingSummary'] = _TEMPLATEMATCHINGSUMMARY

# @@protoc_insertion_point(module_scope)
