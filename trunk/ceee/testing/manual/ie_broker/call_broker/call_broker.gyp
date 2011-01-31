# Copyright (c) 2010 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    '../../../../../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'call_broker',
      'type': 'executable',
      'sources': [
        'call_broker.cc',
      ],
      'defines': [
        '_CONSOLE',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/ceee/common/common.gyp:ceee_common',
        '<(DEPTH)/ceee/ie/plugin/toolband/toolband.gyp:toolband_idl',
        '<(DEPTH)/ceee/ie/common/common.gyp:ie_common',
      ],
    },
  ]
}
