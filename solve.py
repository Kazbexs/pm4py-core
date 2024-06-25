from pm4py.objects.iot import apis
from pm4py.objects.iot.utils import cleaner
from pm4py import read, write, discovery, vis
from pm4py.objects.iot.utils import verifier
from pm4py.objects.log.obj import EventLog, XESExtension
from pm4py.objects.iot.obj import IOTEventLog, IOTEvent, IOTTrace, Point, FilterSet
from pm4py.objects.iot.importer.xes.variants.xmlxes20 import State
from tests.iot_tests import TestCase

from pm4py.objects.iot import get_traces_with_datastream

def count_lines_in_file(path):
    with open(path, 'r') as file:
        return len(file.readlines())


if __name__ == "__main__":

    filename = 'tmpfile.xes'

    pt = Point(id='point1_id', timestamp=State.date_parser.apply('2023-04-28T17:38:20.0747454+02:00'), value='point1_val', source='point1_source', meta=[{'type':'System.String1'}])

    log = read.read_iot_xes(filename)

    trace = log[0]
    print('expected 3, have=', len(trace))

    event = trace[0]
    output_file = 'output_file.xes'

    write.write_iot_xes(log, output_file)

    log2 = read.read_iot_xes(output_file)

    print(log)

    print(log2)
    print(log == log2)

    quit()


#    path, modified = TestCase.MULTIPOINT()
#    path, modified = TestCase.SENSOR_DATA(27)
    path, modified = TestCase.MULTIPOINT()
    print('path =', modified)
    cleaner.rewrite(path, modified)
    expected_log = read.read_iot_xes(modified)
    verifier.verify(expected_log)

    point_mismatch_modified = verifier.MisMatchCounter.POINT_NONE_VALUE
    """
    print("START_LOG===========================================================")
    print(expected_log)
    print("===========================================================")
    print("===========================================================")
    print("===========================================================END_LOG")
    """

    write.write_iot_xes(expected_log, 'tmpfile')

    have_log = read.read_iot_xes('tmpfile.xes')
    verifier.verify(have_log)
    point_mismatch_tmpfile = verifier.MisMatchCounter.POINT_NONE_VALUE

    exp_trace = expected_log[0]
    have_trace = have_log[0]

    print('LINE COUNT TMPFILE =', count_lines_in_file('tmpfile.xes'))
    print('LINE COUNT MODIFIED =', count_lines_in_file(modified))

#    print(expected_event.attributes == have_event.attributes)

#    print(expected_event)
#    print(have_event)
#    print(expected_event == have_event)

#    cleaner.remove_modified(modified)


#    for trace in log:
#        print(trace)
#        for ev in trace:
#            print('ev = ', type(ev))
        
#            print(type(ev), isinstance(ev, IOTEvent))
#            print(vars(ev))
#            print(ev)
#    print(log)

    """
        log._attributes = copy.copy(self._attributes)
        log._extensions = copy.copy(self._extensions)
        log._omni = copy.copy(self._omni)
        log._classifiers = copy.copy(self._classifiers)
        log._properties = copy.copy(self._properties)
    """
#    print(log)
#    print(type(log))

#    log = read.read_xes('../../datasets_usual/L1.xes')
#    process_model = discovery.discover_bpmn_inductive(log)
#    vis.view_bpmn(process_model)
"""
    key = "concept:name"
    for trace in log:
        id = 0
        for event in trace:
#            print(event, type(event))
            print(id, event[key] or trace.attributes[key])
#            print(event)
            id = id + 1
        print(len(trace))

#[[e[key] for e in t] for t in log]
"""

"""
    for trace in log._list:
        print()
        print('TRACE')
        for event in trace._list:
            print('\nEVENT')
            print(event, len(event))
            for k, v in event._dict.items():
#                print(v, type(v))
#                print(type(v['children']))
                print(k, v)

"""
