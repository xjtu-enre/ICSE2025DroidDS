# Appendix

## Mitigable Cases

This section provides supporting evidence for  answering Review A's Question 1, Review B's Question 2, and the weakness mentioned in Review C. 

- **Review A#Q1: You discuss the concept of mitigable design smells and provide predicates for identifying them. Have you conducted any practical experiments or case studies to verify whether these mitigable smells can indeed be eradicated as easily as suggested? If not, are there plans to validate these mitigation strategies empirically?**
- **Review B#Q2: Can you remove/rephrase the unsupported claims?**
- **Review C#Weaknesses: The paper makes multiple claims that are not adequately supported by analysis.**

**Concept description**

| Name          | Description                                                                    |
| ------------- | ------------------------------------------------------------------------------ |
| Case          | The Case where these design smell instances were eliminated in version history |
| From Entity   | The source entity of relation                                                  |
| Relation      | The type of relation                                                           |
| To Entity     | The destination entity of relation                                             |
| Modified Line | The number of modified line to eliminate the design smell                      |
| Code Fragment | The real code fragment of Case in Android project                              |

Specifically, the detailed information of the 24 Cases is shown below, including code entities, dependencies, and source code snippets.

### Case 1

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.weatherTileProvider
- **Modified Line : 2**

### Case 2

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.headsupTileProvider
- **Modified Line : 2**

### Case 3

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.powerButtonTileProvider
- **Modified Line : 2**

### Case 4

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.dataSwitchTileProvider
- **Modified Line : 2**

#### Code Fragment in OmniROM-android11 (Case 1 - Case 4)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
    public QSFactoryImpl(Lazy<QSHost> qsHostLazy,
            Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<WeatherTile> weatherTileProvider, // Case 1
            Provider<HeadsUpTile> headsupTileProvider, // Case 2
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<PowerButtonTile> powerButtonTileProvider, // Case 3
            Provider<DataSwitchTile> dataSwitchTileProvider) { // Case 4
        mQsHostLazy = qsHostLazy;
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mWeatherTileProvider = weatherTileProvider; // Case 1
        mHeadsUpTileProvider = headsupTileProvider; // Case 2
        mScreenshotTileProvider = screenshotTileProvider; 
        mPowerButtonTileProvider = powerButtonTileProvider; // Case 3
        mDataSwitchTileProvider = dataSwitchTileProvider; // Case 4
    }
```

#### Code Fragment in  OmniROM-android12 (Case 1 - Case 4)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
    public QSFactoryImpl(
            Lazy<QSHost> qsHostLazy,
            Provider<CustomTile.Builder> customTileBuilderProvider,
            Provider<WifiTile> wifiTileProvider,
            Provider<InternetTile> internetTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<ReduceBrightColorsTile> reduceBrightColorsTileProvider,
            Provider<CameraToggleTile> cameraToggleTileProvider,
            Provider<MicrophoneToggleTile> microphoneToggleTileProvider,
            Provider<DeviceControlsTile> deviceControlsTileProvider,
            Provider<AlarmTile> alarmTileProvider,
            Provider<QuickAccessWalletTile> quickAccessWalletTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<CaffeineTile> caffeineTileProvider) {
        mQsHostLazy = qsHostLazy;
        mCustomTileBuilderProvider = customTileBuilderProvider;

        mWifiTileProvider = wifiTileProvider;
        mInternetTileProvider = internetTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        mReduceBrightColorsTileProvider = reduceBrightColorsTileProvider;
        mCameraToggleTileProvider = cameraToggleTileProvider;
        mMicrophoneToggleTileProvider = microphoneToggleTileProvider;
        mDeviceControlsTileProvider = deviceControlsTileProvider;
        mAlarmTileProvider = alarmTileProvider;
        mQuickAccessWalletTileProvider = quickAccessWalletTileProvider;

        //Omni
        mAODTileProvider = aodTileProvider;
        mScreenshotTileProvider = screenshotTileProvider;
        mCaffeineTileProvider = caffeineTileProvider;
    }
```

### Case 5

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation: Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.caffeineTileProvider
- **Modified Line : 2**

### Case 6

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.adbOverNetworkProvider
- **Modified Line : 2**

### Case 7

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.scrTileProvider
- **Modified Line : 2**

### Case 8

- From Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl
- Relation : Parameter
- To Entity : com.android.systemui.qs.tileimpl.QSFactoryImpl.QSFactoryImpl.immersiveTileProvider
- **Modified Line : 2**

#### Code Fragment in OmniROM-android10 (Case 5 - Case 8)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
    public QSFactoryImpl(Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<CaffeineTile> caffeineTileProvider, // Case 5
            Provider<AdbOverNetworkTile> adbOverNetworkProvider, // Case 6
            Provider<ScreenrecordTile> scrTileProvider,  // Case 7
            Provider<WeatherTile> weatherTileProvider,
            Provider<HeadsUpTile> headsupTileProvider,
            Provider<ImmersiveTile> immersiveTileProvider, // Case 8
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<DataSwitchTile> dataSwitchTileProvider) {
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mCaffeineTileProvider = caffeineTileProvider; // Case 5
        mAdbOverNetworkProvider = adbOverNetworkProvider; // Case 6
        mScrTileProvider = scrTileProvider;  // Case 7
        mWeatherTileProvider = weatherTileProvider;
        mHeadsUpTileProvider = headsupTileProvider;
        mImmersiveTileProvider = immersiveTileProvider; // Case 8
        mScreenshotTileProvider = screenshotTileProvider;
        mDataSwitchTileProvider = dataSwitchTileProvider;
    }
```

#### Code Fragment in OmniROM-android11 (Case 5 - Case 8)

```java
// packages/SystemUI/src/com/android/systemui/qs/tileimpl/QSFactoryImpl.java
    public QSFactoryImpl(Lazy<QSHost> qsHostLazy,
            Provider<WifiTile> wifiTileProvider,
            Provider<BluetoothTile> bluetoothTileProvider,
            Provider<CellularTile> cellularTileProvider,
            Provider<DndTile> dndTileProvider,
            Provider<ColorInversionTile> colorInversionTileProvider,
            Provider<AirplaneModeTile> airplaneModeTileProvider,
            Provider<WorkModeTile> workModeTileProvider,
            Provider<RotationLockTile> rotationLockTileProvider,
            Provider<FlashlightTile> flashlightTileProvider,
            Provider<LocationTile> locationTileProvider,
            Provider<CastTile> castTileProvider,
            Provider<HotspotTile> hotspotTileProvider,
            Provider<UserTile> userTileProvider,
            Provider<BatterySaverTile> batterySaverTileProvider,
            Provider<DataSaverTile> dataSaverTileProvider,
            Provider<NightDisplayTile> nightDisplayTileProvider,
            Provider<NfcTile> nfcTileProvider,
            Provider<GarbageMonitor.MemoryTile> memoryTileProvider,
            Provider<UiModeNightTile> uiModeNightTileProvider,
            Provider<ScreenRecordTile> screenRecordTileProvider,
            Provider<AODTile> aodTileProvider,
            Provider<WeatherTile> weatherTileProvider,
            Provider<HeadsUpTile> headsupTileProvider,
            Provider<ScreenshotTile> screenshotTileProvider,
            Provider<PowerButtonTile> powerButtonTileProvider,
            Provider<DataSwitchTile> dataSwitchTileProvider) {
        mQsHostLazy = qsHostLazy;
        mWifiTileProvider = wifiTileProvider;
        mBluetoothTileProvider = bluetoothTileProvider;
        mCellularTileProvider = cellularTileProvider;
        mDndTileProvider = dndTileProvider;
        mColorInversionTileProvider = colorInversionTileProvider;
        mAirplaneModeTileProvider = airplaneModeTileProvider;
        mWorkModeTileProvider = workModeTileProvider;
        mRotationLockTileProvider = rotationLockTileProvider;
        mFlashlightTileProvider = flashlightTileProvider;
        mLocationTileProvider = locationTileProvider;
        mCastTileProvider = castTileProvider;
        mHotspotTileProvider = hotspotTileProvider;
        mUserTileProvider = userTileProvider;
        mBatterySaverTileProvider = batterySaverTileProvider;
        mDataSaverTileProvider = dataSaverTileProvider;
        mNightDisplayTileProvider = nightDisplayTileProvider;
        mNfcTileProvider = nfcTileProvider;
        mMemoryTileProvider = memoryTileProvider;
        mUiModeNightTileProvider = uiModeNightTileProvider;
        mScreenRecordTileProvider = screenRecordTileProvider;
        //Omni
        mAODTileProvider = aodTileProvider;
        mWeatherTileProvider = weatherTileProvider;
        mHeadsUpTileProvider = headsupTileProvider;
        mScreenshotTileProvider = screenshotTileProvider; 
        mPowerButtonTileProvider = powerButtonTileProvider;
        mDataSwitchTileProvider = dataSwitchTileProvider;
    }
```

### Case 9

- From Entity : com.android.settingslib.location.SettingsInjector
- Relation : Define
- To Entity : com.android.settingslib.location.SettingsInjector.parseServiceInfo
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 9)

```java
// services/core/java/com/android/server/wm/ActivityStackSupervisor.java
    protected InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle, 
            PackageManager pm) throws XmlPullParserException, IOException { 
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 9)

```java
// services/core/java/com/android/server/wm/ActivityStackSupervisor.java
    private static InjectedSetting parseServiceInfo(ResolveInfo service, UserHandle userHandle,
            PackageManager pm) throws XmlPullParserException, IOException {
        ...
    }
```

### Case 10

- From Entity : com.android.keyguard.EmergencyButton

- Relation : Define

- To Entity : com.android.keyguard.EmergencyButton.updateEmergencyCallButton

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 10)

```java
// services/core/java/com/android/server/wm/RootWindowContainer.java
    public void updateEmergencyCallButton() {
        boolean visible = false;
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 10)

```java
// services/core/java/com/android/server/wm/RootWindowContainer.java
    void updateEmergencyCallButton(boolean isInCall, boolean isVoiceCapable, boolean simLocked) {
        boolean visible = false;
        ...
    }
```

### Case 11

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answerVideo
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 11)

```java
// telecomm/java/android/telecom/ConnectionService.java
    protected void answerVideo(String callId, int videoState) {
        Log.i(this, "answerVideo %s", callId);
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 11)

```java
// telecomm/java/android/telecom/ConnectionService.java
    private void answerVideo(String callId, int videoState) {
        Log.i(this, "answerVideo %s", callId);
        ...
    }
```

### Case 12

- From Entity : android.telecom.ConnectionService
- Relation : Define
- To Entity : android.telecom.ConnectionService.answer
- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 12)

```java
// telecomm/java/android/telecom/ConnectionService.java
    protected void answer(String callId) {
        Log.i(this, "answer %s", callId);
        ...
    }
```

#### Code Fragment in OmniROM-android12 (Case 12)

```java
// telecomm/java/android/telecom/ConnectionService.java    
    private void answer(String callId) {
        Log.i(this, "answer %s", callId);
        ...
    }
```

### Case 13

- From Entity : android.nfc.cardemulation.AidGroup

- Relation : Define

- To Entity : android.nfc.cardemulation.AidGroup.aids

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 13)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected List<String> aids;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 13)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final List<String> aids;
    ...
}
```

### Case 14

- From Entity : android.nfc.cardemulation.AidGroup

- Relation : Define

- To Entity : android.nfc.cardemulation.AidGroup.category

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 14)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected String category;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 14)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final String category;
    ...
}
```

### Case 15

- From Entity : android.nfc.cardemulation.AidGroup

- Relation : Define

- To Entity : android.nfc.cardemulation.AidGroup.description

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 15)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    protected String description;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 15)

```java
// core/java/android/nfc/cardemulation/AidGroup.java
public class AidGroup implements Parcelable {
    ...
    final String description;
    ...
}
```

### Case 16

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mService

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 16)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected ResolveInfo mService;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 16)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final ResolveInfo mService;
    ...
}
```

### Case 17

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mDescription

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 17)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mDescription;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 17)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final String mDescription;
    ...
}
```

### Case 18

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mOnHost

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 18)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mOnHost;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 18)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final boolean mOnHost;
    ...
}
```

### Case 19

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mStaticAidGroups

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 19)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mStaticAidGroups;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 19)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final HashMap<String, AidGroup> mStaticAidGroups;
    ...
}
```

### Case 20

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mDynamicAidGroups

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 20)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected  HashMap<String, AidGroup> mDynamicAidGroups;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 20)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final HashMap<String, AidGroup> mDynamicAidGroups;
    ...
}
```

### Case 21

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mRequiresDeviceUnlock

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 21)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected boolean mRequiresDeviceUnlock;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 21)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final boolean mRequiresDeviceUnlock;
    ...
}
```

### Case 22

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mBannerResourceId

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 22)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mBannerResourceId;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 22)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final int mBannerResourceId;
    ...
}
```

### Case 23

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mUid

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 23)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected int mUid;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 23)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final int mUid;
    ...
}
```

### Case 24

- From Entity : android.nfc.cardemulation.ApduServiceInfo

- Relation : Define

- To Entity : android.nfc.cardemulation.ApduServiceInfo.mSettingsActivityName

- **Modified Line : 1**

#### Code Fragment in OmniROM-android11 (Case 24)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    protected String mSettingsActivityName;
    ...
}
```

#### Code Fragment in OmniROM-android12 (Case 24)

```java
// core/java/android/nfc/cardemulation/ApduServiceInfo.java
public class ApduServiceInfo implements Parcelable {
    ...
    final String mSettingsActivityName;
    ...
}
```

## Table 1 The detailed precision and recall results in RQ2

**Table 1** lists the *Precision* and *Recall* results of conflicts involved with design smells in details, including *\|ConfF|,\|ConfF_cap\|,\|CapF\|*.

| Project | \|ConfF\| | \|ConfF_cap\| | \|CapF\| | Precision | Recall  |
|:------- |:---------:|:-------------:|:--------:|:---------:| ------- |
| A-T     | 60        | 40            | 329      | 12.16%    | 66.67%  |
| A-S     | 183       | 135           | 1463     | 9.23%     | 73.77%  |
| A-R     | 170       | 110           | 333      | 33.03%    | 64.70%  |
| A-Q     | 134       | 95            | 212      | 44.81%    | 70.90%  |
| C-13    | 44        | 22            | 100      | 22.00%    | 50.00%  |
| C-12    | 18        | 1             | 75       | 1.33%     | 5.56%   |
| C-11    | 1         | 1             | 90       | 1.11%     | 100%    |
| L-20.0  | 77        | 52            | 176      | 29.55%    | 67.53%  |
| L-19.1  | 2         | 2             | 263      | 0.76%     | 100.00% |
| L-18.1  | 18        | 10            | 275      | 3.64%     | 55.56%  |
| L-17.1  | 43        | 21            | 270      | 7.78%     | 53.49%  |
| L-16.0  | 23        | 16            | 255      | 6.27%     | 69.57%  |
| O-13.0  | 42        | 26            | 96       | 27.08%    | 61.90%  |
| O-12.0  | 9         | 2             | 100      | 2.00%     | 22.22%  |
| O-11    | 255       | 147           | 419      | 35.08%    | 58.43%  |
| O-10    | 36        | 26            | 247      | 10.53%    | 72.22%  |
| O-9     | 10        | 7             | 199      | 3.52%     | 70.00%  |
| I-E     | 534       | 485           | 2146     | 22.60%    | 90.82%  |
| I-D     | 534       | 502           | 2308     | 21.75%    | 94.01%  |
| I-C     | 534       | 502           | 2246     | 22.35%    | 94.01%  |
| I-B     | 500       | 454           | 2221     | 20.44%    | 90.80%  |
| I-A     | 321       | 266           | 1817     | 14.64%    | 82.87%  |
| Average | 161       | 133           | 711      | 15.98%    | 68.87%  |

## Table 2 Results of Wilcoxon sign-rank test in RQ2

Table 2 presents the Wilcoxon Sign-Rank Test results with P-value of 0.002 and effect size of 0.974. It indicates that the number of code conflict blocks involved with design smell files is significantly larger than that of other files.

| Measure | *P-value* | *effect size* |
|:-------:|:---------:|:-------------:|
| *confB* | 0.002     | 0.974         |

## Table 3 Average conflict count statistics for files with and without design smell involvement

We measured *avg_confB_aff* and *avg_confB_nonaff* to count the average conflict blocks within design smell files and those outside design smell files.

The ***times*** row indicates that the files affected by design smells have been involved in 2 times (indicated by *times* = 2) more conflict blocks than the non-affected files on average.

| *avg_confB_aff* | *avg_confB_nonaff* | *times* |
|:---------------:|:------------------:|:-------:|
| 4               | 2                  | 2       |

## Table 4 Validation results of recurring conflict blocks across **commits** for **Comments** **3.8**

**Table 4**  shows the validation results for recurring conflict block identification across commits. The **Detection Results** column lists the recurring conflict blocks detected automatically, and the **Baseline** column counts recurring conflict blocks in the baseline. Against the baseline, we calculated the precision and recall of the recurring block detection results. The last two columns list the values of recall and precision.

| Project | **Block** | **Baseline** | Detection Results | Precision | Recall |
|:-------:|:---------:|:------------:|:-----------------:|:---------:|:------:|
| A-S     | 261       | 12           | 10                | 100%      | 83.33% |
| A-R     | 202       | 10           | 12                | 83.33%    | 100%   |
| A-Q     | 216       | 10           | 8                 | 100%      | 80%    |
| L-18.1  | 31        | 4            | 4                 | 100%      | 100%   |
| L-17.1  | 95        | 12           | 11                | 100%      | 91.67% |
| O-13.0  | 111       | 6            | 6                 | 100%      | 100%   |
| O-11    | 426       | 26           | 61                | 42.62%    | 100%   |
| Average | 119       | 16           | 22                | 89.42%    | 93.57% |

## Table 5 Validation results of recurring conflict blocks across **versions** for **Comments** **3.8**

**Table 5**  shows the validation results for recurring conflict block identification across versions. The **Detection Results** column lists the recurring conflict blocks detected automatically, and the **Baseline** column counts recurring conflict blocks in the baseline. Against the baseline, we calculated the precision and recall of the recurring block detection results. 

| Project   | **Block** | **Baseline** | Detection Results | Precision | Recall |
|:---------:|:---------:|:------------:|:-----------------:|:---------:|:------:|
| AOSPA     | 819       | 37           | 35                | 100%      | 94.59% |
| LineageOS | 321       | 9            | 9                 | 100%      | 100%   |
| OmniROM   | 623       | 4            | 4                 | 100%      | 100%   |
| Average   | 477       | 17           | 16                | 100%      | 98.20% |

## Table 6 Validation results of recurring conflict blocks across **projects** for **Comments** **3.8**

**Table 6**  shows the validation results for recurring conflict blocks identification across projects. The **Detection Results** column lists the recurring conflict blocks detected automatically, and the **Baseline** column counts recurring conflict blocks in the baseline. Against the baseline, we calculated the precision and recall of the recurring block detection results. 

| **Type**     | **Block** | **Baseline** | Detection Results | Precision | Recall |
|:------------:|:---------:|:------------:|:-----------------:|:---------:|:------:|
| Diff-project | 1906      | 648          | 672               | 96.43%    | 100%   |
