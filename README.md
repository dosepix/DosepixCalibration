# Dosepix Calibration via CNN
Author: Sebastian Schmidt
E-Mail: schm.seb@gmail.com  

### Calibration procedure
- Use DPXControlPython-software (see: https://github.com/dosepix/DPXControlPython) to take measurements with one or multiple Dosepix detectors
- First, call the equalization script (see DPXControlPython documentation for more info)
- The detector system is placed in front of an Am-241 calibration source with additional Mo-XRF target
- ToT-spectra are acquired by calling `dpx.measureToT()`
- Registered data is loaded in the DNNCalib jupyter notebook and calibration performed according to the included remarks
- Resulting calibration parameters per pixel are stored in a `.json` file
