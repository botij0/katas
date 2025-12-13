type ElfDateTime = `${number}*${number}*${number}@${number}|${number}|${number} NP`;

function timeUntilTakeOff(fromTime: ElfDateTime, takeOffTime: ElfDateTime): number {
  const [fyear, fmonth, fday] = fromTime.split("@")[0].split("*");
  const [fhour, fmin, fsec] = fromTime
    .slice(0, fromTime.length - 2)
    .split("@")[1]
    .split("|");

  const [tyear, tmonth, tday] = takeOffTime.split("@")[0].split("*");
  const [thour, tmin, tsec] = takeOffTime
    .slice(0, takeOffTime.length - 2)
    .split("@")[1]
    .split("|");

  const fromTimeDate = new Date(
    `${fyear}-${fmonth}-${fday}T${fhour}:${fmin}:${fsec}`.trim()
  );
  const takeOffTimeDate = new Date(
    `${tyear}-${tmonth}-${tday}T${thour}:${tmin}:${tsec}`.trim()
  );

  return Math.floor((takeOffTimeDate.getTime() - fromTimeDate.getTime()) / 1000);
}

const takeoff = "2025*12*25@00|00|00 NP";
console.log(timeUntilTakeOff("2025*12*25@00|00|12 NP", takeoff));
