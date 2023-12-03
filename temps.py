import wmi

def tempinit():
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        data = {
                "GPU Core" : "0.0C",
                "GPU Fan" : "0.0RPM",
                "CPU Package" : "0.0C"   
                }
        interest = ['GPU Core','GPU Fan','CPU Package', 'CPU Total']
        for sensor in temperature_infos:
            if sensor.name in interest:
                if sensor.SensorType=='Temperature':
                    if sensor.name=='GPU Core':
                        data['GPU Core'] = ' {}C'.format("%.1f"%sensor.Value)
                    else:
                        data['CPU Package'] = ' {}C'.format("%.1f"%sensor.Value)
                elif sensor.name=='Fan':
                    data['GPU Fan'] = ' {}RPM'.format(sensor.Value)+'\n'

        return data


                    
         
          
                 
