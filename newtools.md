var $e = Object.defineProperty
  , Se = Object.defineProperties;
var Ee = Object.getOwnPropertyDescriptors;
var se = Object.getOwnPropertySymbols;
var Oe = Object.prototype.hasOwnProperty
  , ke = Object.prototype.propertyIsEnumerable;
var ne = (r, e, t) => e in r ? $e(r, e, {
    enumerable: !0,
    configurable: !0,
    writable: !0,
    value: t
}) : r[e] = t
  , ie = (r, e) => {
    for (var t in e || (e = {}))
        Oe.call(e, t) && ne(r, t, e[t]);
    if (se)
        for (var t of se(e))
            ke.call(e, t) && ne(r, t, e[t]);
    return r
}
  , ue = (r, e) => Se(r, Ee(e));
var le = (r, e, t) => (ne(r, typeof e != "symbol" ? e + "" : e, t),
t);
var b = (r, e, t) => new Promise( (a, n) => {
    var i = l => {
        try {
            d(t.next(l))
        } catch (c) {
            n(c)
        }
    }
      , o = l => {
        try {
            d(t.throw(l))
        } catch (c) {
            n(c)
        }
    }
      , d = l => l.done ? a(l.value) : Promise.resolve(l.value).then(i, o);
    d((t = t.apply(r, e)).next())
}
);
import {l as s, r as k, j as u} from "./index.b6f58f40.js";
function Z(r) {
    "@babel/helpers - typeof";
    return Z = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(e) {
        return typeof e
    }
    : function(e) {
        return e && typeof Symbol == "function" && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
    }
    ,
    Z(r)
}
function y(r, e) {
    if (e.length < r)
        throw new TypeError(r + " argument" + (r > 1 ? "s" : "") + " required, but only " + e.length + " present")
}
function Ne(r) {
    return y(1, arguments),
    r instanceof Date || Z(r) === "object" && Object.prototype.toString.call(r) === "[object Date]"
}
function T(r) {
    y(1, arguments);
    var e = Object.prototype.toString.call(r);
    return r instanceof Date || Z(r) === "object" && e === "[object Date]" ? new Date(r.getTime()) : typeof r == "number" || e === "[object Number]" ? new Date(r) : ((typeof r == "string" || e === "[object String]") && typeof console != "undefined" && (console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments"),
    console.warn(new Error().stack)),
    new Date(NaN))
}
function We(r) {
    if (y(1, arguments),
    !Ne(r) && typeof r != "number")
        return !1;
    var e = T(r);
    return !isNaN(Number(e))
}
function B(r) {
    if (r === null || r === !0 || r === !1)
        return NaN;
    var e = Number(r);
    return isNaN(e) ? e : e < 0 ? Math.ceil(e) : Math.floor(e)
}
function Ie(r, e) {
    y(2, arguments);
    var t = T(r).getTime()
      , a = B(e);
    return new Date(t + a)
}
function je(r, e) {
    y(2, arguments);
    var t = B(e);
    return Ie(r, -t)
}
var _e = 864e5;
function Ae(r) {
    y(1, arguments);
    var e = T(r)
      , t = e.getTime();
    e.setUTCMonth(0, 1),
    e.setUTCHours(0, 0, 0, 0);
    var a = e.getTime()
      , n = t - a;
    return Math.floor(n / _e) + 1
}
function ee(r) {
    y(1, arguments);
    var e = 1
      , t = T(r)
      , a = t.getUTCDay()
      , n = (a < e ? 7 : 0) + a - e;
    return t.setUTCDate(t.getUTCDate() - n),
    t.setUTCHours(0, 0, 0, 0),
    t
}
function be(r) {
    y(1, arguments);
    var e = T(r)
      , t = e.getUTCFullYear()
      , a = new Date(0);
    a.setUTCFullYear(t + 1, 0, 4),
    a.setUTCHours(0, 0, 0, 0);
    var n = ee(a)
      , i = new Date(0);
    i.setUTCFullYear(t, 0, 4),
    i.setUTCHours(0, 0, 0, 0);
    var o = ee(i);
    return e.getTime() >= n.getTime() ? t + 1 : e.getTime() >= o.getTime() ? t : t - 1
}
function Ue(r) {
    y(1, arguments);
    var e = be(r)
      , t = new Date(0);
    t.setUTCFullYear(e, 0, 4),
    t.setUTCHours(0, 0, 0, 0);
    var a = ee(t);
    return a
}
var Ge = 6048e5;
function Ye(r) {
    y(1, arguments);
    var e = T(r)
      , t = ee(e).getTime() - Ue(e).getTime();
    return Math.round(t / Ge) + 1
}
var Re = {};
function te() {
    return Re
}
function H(r, e) {
    var t, a, n, i, o, d, l, c;
    y(1, arguments);
    var p = te()
      , f = B((t = (a = (n = (i = e == null ? void 0 : e.weekStartsOn) !== null && i !== void 0 ? i : e == null || (o = e.locale) === null || o === void 0 || (d = o.options) === null || d === void 0 ? void 0 : d.weekStartsOn) !== null && n !== void 0 ? n : p.weekStartsOn) !== null && a !== void 0 ? a : (l = p.locale) === null || l === void 0 || (c = l.options) === null || c === void 0 ? void 0 : c.weekStartsOn) !== null && t !== void 0 ? t : 0);
    if (!(f >= 0 && f <= 6))
        throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");
    var h = T(r)
      , g = h.getUTCDay()
      , P = (g < f ? 7 : 0) + g - f;
    return h.setUTCDate(h.getUTCDate() - P),
    h.setUTCHours(0, 0, 0, 0),
    h
}
function Pe(r, e) {
    var t, a, n, i, o, d, l, c;
    y(1, arguments);
    var p = T(r)
      , f = p.getUTCFullYear()
      , h = te()
      , g = B((t = (a = (n = (i = e == null ? void 0 : e.firstWeekContainsDate) !== null && i !== void 0 ? i : e == null || (o = e.locale) === null || o === void 0 || (d = o.options) === null || d === void 0 ? void 0 : d.firstWeekContainsDate) !== null && n !== void 0 ? n : h.firstWeekContainsDate) !== null && a !== void 0 ? a : (l = h.locale) === null || l === void 0 || (c = l.options) === null || c === void 0 ? void 0 : c.firstWeekContainsDate) !== null && t !== void 0 ? t : 1);
    if (!(g >= 1 && g <= 7))
        throw new RangeError("firstWeekContainsDate must be between 1 and 7 inclusively");
    var P = new Date(0);
    P.setUTCFullYear(f + 1, 0, g),
    P.setUTCHours(0, 0, 0, 0);
    var F = H(P, e)
      , N = new Date(0);
    N.setUTCFullYear(f, 0, g),
    N.setUTCHours(0, 0, 0, 0);
    var U = H(N, e);
    return p.getTime() >= F.getTime() ? f + 1 : p.getTime() >= U.getTime() ? f : f - 1
}
function Be(r, e) {
    var t, a, n, i, o, d, l, c;
    y(1, arguments);
    var p = te()
      , f = B((t = (a = (n = (i = e == null ? void 0 : e.firstWeekContainsDate) !== null && i !== void 0 ? i : e == null || (o = e.locale) === null || o === void 0 || (d = o.options) === null || d === void 0 ? void 0 : d.firstWeekContainsDate) !== null && n !== void 0 ? n : p.firstWeekContainsDate) !== null && a !== void 0 ? a : (l = p.locale) === null || l === void 0 || (c = l.options) === null || c === void 0 ? void 0 : c.firstWeekContainsDate) !== null && t !== void 0 ? t : 1)
      , h = Pe(r, e)
      , g = new Date(0);
    g.setUTCFullYear(h, 0, f),
    g.setUTCHours(0, 0, 0, 0);
    var P = H(g, e);
    return P
}
var Fe = 6048e5;
function Le(r, e) {
    y(1, arguments);
    var t = T(r)
      , a = H(t, e).getTime() - Be(t, e).getTime();
    return Math.round(a / Fe) + 1
}
function v(r, e) {
    for (var t = r < 0 ? "-" : "", a = Math.abs(r).toString(); a.length < e; )
        a = "0" + a;
    return t + a
}
var qe = {
    y: function(e, t) {
        var a = e.getUTCFullYear()
          , n = a > 0 ? a : 1 - a;
        return v(t === "yy" ? n % 100 : n, t.length)
    },
    M: function(e, t) {
        var a = e.getUTCMonth();
        return t === "M" ? String(a + 1) : v(a + 1, 2)
    },
    d: function(e, t) {
        return v(e.getUTCDate(), t.length)
    },
    a: function(e, t) {
        var a = e.getUTCHours() / 12 >= 1 ? "pm" : "am";
        switch (t) {
        case "a":
        case "aa":
            return a.toUpperCase();
        case "aaa":
            return a;
        case "aaaaa":
            return a[0];
        case "aaaa":
        default:
            return a === "am" ? "a.m." : "p.m."
        }
    },
    h: function(e, t) {
        return v(e.getUTCHours() % 12 || 12, t.length)
    },
    H: function(e, t) {
        return v(e.getUTCHours(), t.length)
    },
    m: function(e, t) {
        return v(e.getUTCMinutes(), t.length)
    },
    s: function(e, t) {
        return v(e.getUTCSeconds(), t.length)
    },
    S: function(e, t) {
        var a = t.length
          , n = e.getUTCMilliseconds()
          , i = Math.floor(n * Math.pow(10, a - 3));
        return v(i, t.length)
    }
};
const _ = qe;
var L = {
    am: "am",
    pm: "pm",
    midnight: "midnight",
    noon: "noon",
    morning: "morning",
    afternoon: "afternoon",
    evening: "evening",
    night: "night"
}
  , He = {
    G: function(e, t, a) {
        var n = e.getUTCFullYear() > 0 ? 1 : 0;
        switch (t) {
        case "G":
        case "GG":
        case "GGG":
            return a.era(n, {
                width: "abbreviated"
            });
        case "GGGGG":
            return a.era(n, {
                width: "narrow"
            });
        case "GGGG":
        default:
            return a.era(n, {
                width: "wide"
            })
        }
    },
    y: function(e, t, a) {
        if (t === "yo") {
            var n = e.getUTCFullYear()
              , i = n > 0 ? n : 1 - n;
            return a.ordinalNumber(i, {
                unit: "year"
            })
        }
        return _.y(e, t)
    },
    Y: function(e, t, a, n) {
        var i = Pe(e, n)
          , o = i > 0 ? i : 1 - i;
        if (t === "YY") {
            var d = o % 100;
            return v(d, 2)
        }
        return t === "Yo" ? a.ordinalNumber(o, {
            unit: "year"
        }) : v(o, t.length)
    },
    R: function(e, t) {
        var a = be(e);
        return v(a, t.length)
    },
    u: function(e, t) {
        var a = e.getUTCFullYear();
        return v(a, t.length)
    },
    Q: function(e, t, a) {
        var n = Math.ceil((e.getUTCMonth() + 1) / 3);
        switch (t) {
        case "Q":
            return String(n);
        case "QQ":
            return v(n, 2);
        case "Qo":
            return a.ordinalNumber(n, {
                unit: "quarter"
            });
        case "QQQ":
            return a.quarter(n, {
                width: "abbreviated",
                context: "formatting"
            });
        case "QQQQQ":
            return a.quarter(n, {
                width: "narrow",
                context: "formatting"
            });
        case "QQQQ":
        default:
            return a.quarter(n, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    q: function(e, t, a) {
        var n = Math.ceil((e.getUTCMonth() + 1) / 3);
        switch (t) {
        case "q":
            return String(n);
        case "qq":
            return v(n, 2);
        case "qo":
            return a.ordinalNumber(n, {
                unit: "quarter"
            });
        case "qqq":
            return a.quarter(n, {
                width: "abbreviated",
                context: "standalone"
            });
        case "qqqqq":
            return a.quarter(n, {
                width: "narrow",
                context: "standalone"
            });
        case "qqqq":
        default:
            return a.quarter(n, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    M: function(e, t, a) {
        var n = e.getUTCMonth();
        switch (t) {
        case "M":
        case "MM":
            return _.M(e, t);
        case "Mo":
            return a.ordinalNumber(n + 1, {
                unit: "month"
            });
        case "MMM":
            return a.month(n, {
                width: "abbreviated",
                context: "formatting"
            });
        case "MMMMM":
            return a.month(n, {
                width: "narrow",
                context: "formatting"
            });
        case "MMMM":
        default:
            return a.month(n, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    L: function(e, t, a) {
        var n = e.getUTCMonth();
        switch (t) {
        case "L":
            return String(n + 1);
        case "LL":
            return v(n + 1, 2);
        case "Lo":
            return a.ordinalNumber(n + 1, {
                unit: "month"
            });
        case "LLL":
            return a.month(n, {
                width: "abbreviated",
                context: "standalone"
            });
        case "LLLLL":
            return a.month(n, {
                width: "narrow",
                context: "standalone"
            });
        case "LLLL":
        default:
            return a.month(n, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    w: function(e, t, a, n) {
        var i = Le(e, n);
        return t === "wo" ? a.ordinalNumber(i, {
            unit: "week"
        }) : v(i, t.length)
    },
    I: function(e, t, a) {
        var n = Ye(e);
        return t === "Io" ? a.ordinalNumber(n, {
            unit: "week"
        }) : v(n, t.length)
    },
    d: function(e, t, a) {
        return t === "do" ? a.ordinalNumber(e.getUTCDate(), {
            unit: "date"
        }) : _.d(e, t)
    },
    D: function(e, t, a) {
        var n = Ae(e);
        return t === "Do" ? a.ordinalNumber(n, {
            unit: "dayOfYear"
        }) : v(n, t.length)
    },
    E: function(e, t, a) {
        var n = e.getUTCDay();
        switch (t) {
        case "E":
        case "EE":
        case "EEE":
            return a.day(n, {
                width: "abbreviated",
                context: "formatting"
            });
        case "EEEEE":
            return a.day(n, {
                width: "narrow",
                context: "formatting"
            });
        case "EEEEEE":
            return a.day(n, {
                width: "short",
                context: "formatting"
            });
        case "EEEE":
        default:
            return a.day(n, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    e: function(e, t, a, n) {
        var i = e.getUTCDay()
          , o = (i - n.weekStartsOn + 8) % 7 || 7;
        switch (t) {
        case "e":
            return String(o);
        case "ee":
            return v(o, 2);
        case "eo":
            return a.ordinalNumber(o, {
                unit: "day"
            });
        case "eee":
            return a.day(i, {
                width: "abbreviated",
                context: "formatting"
            });
        case "eeeee":
            return a.day(i, {
                width: "narrow",
                context: "formatting"
            });
        case "eeeeee":
            return a.day(i, {
                width: "short",
                context: "formatting"
            });
        case "eeee":
        default:
            return a.day(i, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    c: function(e, t, a, n) {
        var i = e.getUTCDay()
          , o = (i - n.weekStartsOn + 8) % 7 || 7;
        switch (t) {
        case "c":
            return String(o);
        case "cc":
            return v(o, t.length);
        case "co":
            return a.ordinalNumber(o, {
                unit: "day"
            });
        case "ccc":
            return a.day(i, {
                width: "abbreviated",
                context: "standalone"
            });
        case "ccccc":
            return a.day(i, {
                width: "narrow",
                context: "standalone"
            });
        case "cccccc":
            return a.day(i, {
                width: "short",
                context: "standalone"
            });
        case "cccc":
        default:
            return a.day(i, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    i: function(e, t, a) {
        var n = e.getUTCDay()
          , i = n === 0 ? 7 : n;
        switch (t) {
        case "i":
            return String(i);
        case "ii":
            return v(i, t.length);
        case "io":
            return a.ordinalNumber(i, {
                unit: "day"
            });
        case "iii":
            return a.day(n, {
                width: "abbreviated",
                context: "formatting"
            });
        case "iiiii":
            return a.day(n, {
                width: "narrow",
                context: "formatting"
            });
        case "iiiiii":
            return a.day(n, {
                width: "short",
                context: "formatting"
            });
        case "iiii":
        default:
            return a.day(n, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    a: function(e, t, a) {
        var n = e.getUTCHours()
          , i = n / 12 >= 1 ? "pm" : "am";
        switch (t) {
        case "a":
        case "aa":
            return a.dayPeriod(i, {
                width: "abbreviated",
                context: "formatting"
            });
        case "aaa":
            return a.dayPeriod(i, {
                width: "abbreviated",
                context: "formatting"
            }).toLowerCase();
        case "aaaaa":
            return a.dayPeriod(i, {
                width: "narrow",
                context: "formatting"
            });
        case "aaaa":
        default:
            return a.dayPeriod(i, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    b: function(e, t, a) {
        var n = e.getUTCHours(), i;
        switch (n === 12 ? i = L.noon : n === 0 ? i = L.midnight : i = n / 12 >= 1 ? "pm" : "am",
        t) {
        case "b":
        case "bb":
            return a.dayPeriod(i, {
                width: "abbreviated",
                context: "formatting"
            });
        case "bbb":
            return a.dayPeriod(i, {
                width: "abbreviated",
                context: "formatting"
            }).toLowerCase();
        case "bbbbb":
            return a.dayPeriod(i, {
                width: "narrow",
                context: "formatting"
            });
        case "bbbb":
        default:
            return a.dayPeriod(i, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    B: function(e, t, a) {
        var n = e.getUTCHours(), i;
        switch (n >= 17 ? i = L.evening : n >= 12 ? i = L.afternoon : n >= 4 ? i = L.morning : i = L.night,
        t) {
        case "B":
        case "BB":
        case "BBB":
            return a.dayPeriod(i, {
                width: "abbreviated",
                context: "formatting"
            });
        case "BBBBB":
            return a.dayPeriod(i, {
                width: "narrow",
                context: "formatting"
            });
        case "BBBB":
        default:
            return a.dayPeriod(i, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    h: function(e, t, a) {
        if (t === "ho") {
            var n = e.getUTCHours() % 12;
            return n === 0 && (n = 12),
            a.ordinalNumber(n, {
                unit: "hour"
            })
        }
        return _.h(e, t)
    },
    H: function(e, t, a) {
        return t === "Ho" ? a.ordinalNumber(e.getUTCHours(), {
            unit: "hour"
        }) : _.H(e, t)
    },
    K: function(e, t, a) {
        var n = e.getUTCHours() % 12;
        return t === "Ko" ? a.ordinalNumber(n, {
            unit: "hour"
        }) : v(n, t.length)
    },
    k: function(e, t, a) {
        var n = e.getUTCHours();
        return n === 0 && (n = 24),
        t === "ko" ? a.ordinalNumber(n, {
            unit: "hour"
        }) : v(n, t.length)
    },
    m: function(e, t, a) {
        return t === "mo" ? a.ordinalNumber(e.getUTCMinutes(), {
            unit: "minute"
        }) : _.m(e, t)
    },
    s: function(e, t, a) {
        return t === "so" ? a.ordinalNumber(e.getUTCSeconds(), {
            unit: "second"
        }) : _.s(e, t)
    },
    S: function(e, t) {
        return _.S(e, t)
    },
    X: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = i.getTimezoneOffset();
        if (o === 0)
            return "Z";
        switch (t) {
        case "X":
            return ce(o);
        case "XXXX":
        case "XX":
            return R(o);
        case "XXXXX":
        case "XXX":
        default:
            return R(o, ":")
        }
    },
    x: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = i.getTimezoneOffset();
        switch (t) {
        case "x":
            return ce(o);
        case "xxxx":
        case "xx":
            return R(o);
        case "xxxxx":
        case "xxx":
        default:
            return R(o, ":")
        }
    },
    O: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = i.getTimezoneOffset();
        switch (t) {
        case "O":
        case "OO":
        case "OOO":
            return "GMT" + de(o, ":");
        case "OOOO":
        default:
            return "GMT" + R(o, ":")
        }
    },
    z: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = i.getTimezoneOffset();
        switch (t) {
        case "z":
        case "zz":
        case "zzz":
            return "GMT" + de(o, ":");
        case "zzzz":
        default:
            return "GMT" + R(o, ":")
        }
    },
    t: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = Math.floor(i.getTime() / 1e3);
        return v(o, t.length)
    },
    T: function(e, t, a, n) {
        var i = n._originalDate || e
          , o = i.getTime();
        return v(o, t.length)
    }
};
function de(r, e) {
    var t = r > 0 ? "-" : "+"
      , a = Math.abs(r)
      , n = Math.floor(a / 60)
      , i = a % 60;
    if (i === 0)
        return t + String(n);
    var o = e || "";
    return t + String(n) + o + v(i, 2)
}
function ce(r, e) {
    if (r % 60 === 0) {
        var t = r > 0 ? "-" : "+";
        return t + v(Math.abs(r) / 60, 2)
    }
    return R(r, e)
}
function R(r, e) {
    var t = e || ""
      , a = r > 0 ? "-" : "+"
      , n = Math.abs(r)
      , i = v(Math.floor(n / 60), 2)
      , o = v(n % 60, 2);
    return a + i + t + o
}
const Xe = He;
var fe = function(e, t) {
    switch (e) {
    case "P":
        return t.date({
            width: "short"
        });
    case "PP":
        return t.date({
            width: "medium"
        });
    case "PPP":
        return t.date({
            width: "long"
        });
    case "PPPP":
    default:
        return t.date({
            width: "full"
        })
    }
}
  , Te = function(e, t) {
    switch (e) {
    case "p":
        return t.time({
            width: "short"
        });
    case "pp":
        return t.time({
            width: "medium"
        });
    case "ppp":
        return t.time({
            width: "long"
        });
    case "pppp":
    default:
        return t.time({
            width: "full"
        })
    }
}
  , Ve = function(e, t) {
    var a = e.match(/(P+)(p+)?/) || []
      , n = a[1]
      , i = a[2];
    if (!i)
        return fe(e, t);
    var o;
    switch (n) {
    case "P":
        o = t.dateTime({
            width: "short"
        });
        break;
    case "PP":
        o = t.dateTime({
            width: "medium"
        });
        break;
    case "PPP":
        o = t.dateTime({
            width: "long"
        });
        break;
    case "PPPP":
    default:
        o = t.dateTime({
            width: "full"
        });
        break
    }
    return o.replace("{{date}}", fe(n, t)).replace("{{time}}", Te(i, t))
}
  , Qe = {
    p: Te,
    P: Ve
};
const Je = Qe;
function ze(r) {
    var e = new Date(Date.UTC(r.getFullYear(), r.getMonth(), r.getDate(), r.getHours(), r.getMinutes(), r.getSeconds(), r.getMilliseconds()));
    return e.setUTCFullYear(r.getFullYear()),
    r.getTime() - e.getTime()
}
var Ke = ["D", "DD"]
  , Ze = ["YY", "YYYY"];
function et(r) {
    return Ke.indexOf(r) !== -1
}
function tt(r) {
    return Ze.indexOf(r) !== -1
}
function he(r, e, t) {
    if (r === "YYYY")
        throw new RangeError("Use `yyyy` instead of `YYYY` (in `".concat(e, "`) for formatting years to the input `").concat(t, "`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md"));
    if (r === "YY")
        throw new RangeError("Use `yy` instead of `YY` (in `".concat(e, "`) for formatting years to the input `").concat(t, "`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md"));
    if (r === "D")
        throw new RangeError("Use `d` instead of `D` (in `".concat(e, "`) for formatting days of the month to the input `").concat(t, "`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md"));
    if (r === "DD")
        throw new RangeError("Use `dd` instead of `DD` (in `".concat(e, "`) for formatting days of the month to the input `").concat(t, "`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md"))
}
var rt = {
    lessThanXSeconds: {
        one: "less than a second",
        other: "less than {{count}} seconds"
    },
    xSeconds: {
        one: "1 second",
        other: "{{count}} seconds"
    },
    halfAMinute: "half a minute",
    lessThanXMinutes: {
        one: "less than a minute",
        other: "less than {{count}} minutes"
    },
    xMinutes: {
        one: "1 minute",
        other: "{{count}} minutes"
    },
    aboutXHours: {
        one: "about 1 hour",
        other: "about {{count}} hours"
    },
    xHours: {
        one: "1 hour",
        other: "{{count}} hours"
    },
    xDays: {
        one: "1 day",
        other: "{{count}} days"
    },
    aboutXWeeks: {
        one: "about 1 week",
        other: "about {{count}} weeks"
    },
    xWeeks: {
        one: "1 week",
        other: "{{count}} weeks"
    },
    aboutXMonths: {
        one: "about 1 month",
        other: "about {{count}} months"
    },
    xMonths: {
        one: "1 month",
        other: "{{count}} months"
    },
    aboutXYears: {
        one: "about 1 year",
        other: "about {{count}} years"
    },
    xYears: {
        one: "1 year",
        other: "{{count}} years"
    },
    overXYears: {
        one: "over 1 year",
        other: "over {{count}} years"
    },
    almostXYears: {
        one: "almost 1 year",
        other: "almost {{count}} years"
    }
}
  , at = function(e, t, a) {
    var n, i = rt[e];
    return typeof i == "string" ? n = i : t === 1 ? n = i.one : n = i.other.replace("{{count}}", t.toString()),
    a != null && a.addSuffix ? a.comparison && a.comparison > 0 ? "in " + n : n + " ago" : n
};
const nt = at;
function q(r) {
    return function() {
        var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {}
          , t = e.width ? String(e.width) : r.defaultWidth
          , a = r.formats[t] || r.formats[r.defaultWidth];
        return a
    }
}
var it = {
    full: "EEEE, MMMM do, y",
    long: "MMMM do, y",
    medium: "MMM d, y",
    short: "MM/dd/yyyy"
}
  , ot = {
    full: "h:mm:ss a zzzz",
    long: "h:mm:ss a z",
    medium: "h:mm:ss a",
    short: "h:mm a"
}
  , st = {
    full: "{{date}} 'at' {{time}}",
    long: "{{date}} 'at' {{time}}",
    medium: "{{date}}, {{time}}",
    short: "{{date}}, {{time}}"
}
  , ut = {
    date: q({
        formats: it,
        defaultWidth: "full"
    }),
    time: q({
        formats: ot,
        defaultWidth: "full"
    }),
    dateTime: q({
        formats: st,
        defaultWidth: "full"
    })
};
const lt = ut;
var dt = {
    lastWeek: "'last' eeee 'at' p",
    yesterday: "'yesterday at' p",
    today: "'today at' p",
    tomorrow: "'tomorrow at' p",
    nextWeek: "eeee 'at' p",
    other: "P"
}
  , ct = function(e, t, a, n) {
    return dt[e]
};
const ft = ct;
function W(r) {
    return function(e, t) {
        var a = t != null && t.context ? String(t.context) : "standalone", n;
        if (a === "formatting" && r.formattingValues) {
            var i = r.defaultFormattingWidth || r.defaultWidth
              , o = t != null && t.width ? String(t.width) : i;
            n = r.formattingValues[o] || r.formattingValues[i]
        } else {
            var d = r.defaultWidth
              , l = t != null && t.width ? String(t.width) : r.defaultWidth;
            n = r.values[l] || r.values[d]
        }
        var c = r.argumentCallback ? r.argumentCallback(e) : e;
        return n[c]
    }
}
var ht = {
    narrow: ["B", "A"],
    abbreviated: ["BC", "AD"],
    wide: ["Before Christ", "Anno Domini"]
}
  , mt = {
    narrow: ["1", "2", "3", "4"],
    abbreviated: ["Q1", "Q2", "Q3", "Q4"],
    wide: ["1st quarter", "2nd quarter", "3rd quarter", "4th quarter"]
}
  , vt = {
    narrow: ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"],
    abbreviated: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    wide: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
}
  , gt = {
    narrow: ["S", "M", "T", "W", "T", "F", "S"],
    short: ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"],
    abbreviated: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    wide: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
}
  , yt = {
    narrow: {
        am: "a",
        pm: "p",
        midnight: "mi",
        noon: "n",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    },
    abbreviated: {
        am: "AM",
        pm: "PM",
        midnight: "midnight",
        noon: "noon",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    },
    wide: {
        am: "a.m.",
        pm: "p.m.",
        midnight: "midnight",
        noon: "noon",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    }
}
  , pt = {
    narrow: {
        am: "a",
        pm: "p",
        midnight: "mi",
        noon: "n",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    },
    abbreviated: {
        am: "AM",
        pm: "PM",
        midnight: "midnight",
        noon: "noon",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    },
    wide: {
        am: "a.m.",
        pm: "p.m.",
        midnight: "midnight",
        noon: "noon",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    }
}
  , wt = function(e, t) {
    var a = Number(e)
      , n = a % 100;
    if (n > 20 || n < 10)
        switch (n % 10) {
        case 1:
            return a + "st";
        case 2:
            return a + "nd";
        case 3:
            return a + "rd"
        }
    return a + "th"
}
  , bt = {
    ordinalNumber: wt,
    era: W({
        values: ht,
        defaultWidth: "wide"
    }),
    quarter: W({
        values: mt,
        defaultWidth: "wide",
        argumentCallback: function(e) {
            return e - 1
        }
    }),
    month: W({
        values: vt,
        defaultWidth: "wide"
    }),
    day: W({
        values: gt,
        defaultWidth: "wide"
    }),
    dayPeriod: W({
        values: yt,
        defaultWidth: "wide",
        formattingValues: pt,
        defaultFormattingWidth: "wide"
    })
};
const Pt = bt;
function I(r) {
    return function(e) {
        var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}
          , a = t.width
          , n = a && r.matchPatterns[a] || r.matchPatterns[r.defaultMatchWidth]
          , i = e.match(n);
        if (!i)
            return null;
        var o = i[0], d = a && r.parsePatterns[a] || r.parsePatterns[r.defaultParseWidth], l = Array.isArray(d) ? Dt(d, function(f) {
            return f.test(o)
        }) : Tt(d, function(f) {
            return f.test(o)
        }), c;
        c = r.valueCallback ? r.valueCallback(l) : l,
        c = t.valueCallback ? t.valueCallback(c) : c;
        var p = e.slice(o.length);
        return {
            value: c,
            rest: p
        }
    }
}
function Tt(r, e) {
    for (var t in r)
        if (r.hasOwnProperty(t) && e(r[t]))
            return t
}
function Dt(r, e) {
    for (var t = 0; t < r.length; t++)
        if (e(r[t]))
            return t
}
function De(r) {
    return function(e) {
        var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}
          , a = e.match(r.matchPattern);
        if (!a)
            return null;
        var n = a[0]
          , i = e.match(r.parsePattern);
        if (!i)
            return null;
        var o = r.valueCallback ? r.valueCallback(i[0]) : i[0];
        o = t.valueCallback ? t.valueCallback(o) : o;
        var d = e.slice(n.length);
        return {
            value: o,
            rest: d
        }
    }
}
var Ct = /^(\d+)(th|st|nd|rd)?/i
  , Mt = /\d+/i
  , xt = {
    narrow: /^(b|a)/i,
    abbreviated: /^(b\.?\s?c\.?|b\.?\s?c\.?\s?e\.?|a\.?\s?d\.?|c\.?\s?e\.?)/i,
    wide: /^(before christ|before common era|anno domini|common era)/i
}
  , $t = {
    any: [/^b/i, /^(a|c)/i]
}
  , St = {
    narrow: /^[1234]/i,
    abbreviated: /^q[1234]/i,
    wide: /^[1234](th|st|nd|rd)? quarter/i
}
  , Et = {
    any: [/1/i, /2/i, /3/i, /4/i]
}
  , Ot = {
    narrow: /^[jfmasond]/i,
    abbreviated: /^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)/i,
    wide: /^(january|february|march|april|may|june|july|august|september|october|november|december)/i
}
  , kt = {
    narrow: [/^j/i, /^f/i, /^m/i, /^a/i, /^m/i, /^j/i, /^j/i, /^a/i, /^s/i, /^o/i, /^n/i, /^d/i],
    any: [/^ja/i, /^f/i, /^mar/i, /^ap/i, /^may/i, /^jun/i, /^jul/i, /^au/i, /^s/i, /^o/i, /^n/i, /^d/i]
}
  , Nt = {
    narrow: /^[smtwf]/i,
    short: /^(su|mo|tu|we|th|fr|sa)/i,
    abbreviated: /^(sun|mon|tue|wed|thu|fri|sat)/i,
    wide: /^(sunday|monday|tuesday|wednesday|thursday|friday|saturday)/i
}
  , Wt = {
    narrow: [/^s/i, /^m/i, /^t/i, /^w/i, /^t/i, /^f/i, /^s/i],
    any: [/^su/i, /^m/i, /^tu/i, /^w/i, /^th/i, /^f/i, /^sa/i]
}
  , It = {
    narrow: /^(a|p|mi|n|(in the|at) (morning|afternoon|evening|night))/i,
    any: /^([ap]\.?\s?m\.?|midnight|noon|(in the|at) (morning|afternoon|evening|night))/i
}
  , jt = {
    any: {
        am: /^a/i,
        pm: /^p/i,
        midnight: /^mi/i,
        noon: /^no/i,
        morning: /morning/i,
        afternoon: /afternoon/i,
        evening: /evening/i,
        night: /night/i
    }
}
  , _t = {
    ordinalNumber: De({
        matchPattern: Ct,
        parsePattern: Mt,
        valueCallback: function(e) {
            return parseInt(e, 10)
        }
    }),
    era: I({
        matchPatterns: xt,
        defaultMatchWidth: "wide",
        parsePatterns: $t,
        defaultParseWidth: "any"
    }),
    quarter: I({
        matchPatterns: St,
        defaultMatchWidth: "wide",
        parsePatterns: Et,
        defaultParseWidth: "any",
        valueCallback: function(e) {
            return e + 1
        }
    }),
    month: I({
        matchPatterns: Ot,
        defaultMatchWidth: "wide",
        parsePatterns: kt,
        defaultParseWidth: "any"
    }),
    day: I({
        matchPatterns: Nt,
        defaultMatchWidth: "wide",
        parsePatterns: Wt,
        defaultParseWidth: "any"
    }),
    dayPeriod: I({
        matchPatterns: It,
        defaultMatchWidth: "any",
        parsePatterns: jt,
        defaultParseWidth: "any"
    })
};
const At = _t;
var Ut = {
    code: "en-US",
    formatDistance: nt,
    formatLong: lt,
    formatRelative: ft,
    localize: Pt,
    match: At,
    options: {
        weekStartsOn: 0,
        firstWeekContainsDate: 1
    }
};
const Gt = Ut;
var Yt = /[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g
  , Rt = /P+p+|P+|p+|''|'(''|[^'])+('|$)|./g
  , Bt = /^'([^]*?)'?$/
  , Ft = /''/g
  , Lt = /[a-zA-Z]/;
function A(r, e, t) {
    var a, n, i, o, d, l, c, p, f, h, g, P, F, N, U, X, V, Q;
    y(2, arguments);
    var re = String(e)
      , G = te()
      , m = (a = (n = t == null ? void 0 : t.locale) !== null && n !== void 0 ? n : G.locale) !== null && a !== void 0 ? a : Gt
      , w = B((i = (o = (d = (l = t == null ? void 0 : t.firstWeekContainsDate) !== null && l !== void 0 ? l : t == null || (c = t.locale) === null || c === void 0 || (p = c.options) === null || p === void 0 ? void 0 : p.firstWeekContainsDate) !== null && d !== void 0 ? d : G.firstWeekContainsDate) !== null && o !== void 0 ? o : (f = G.locale) === null || f === void 0 || (h = f.options) === null || h === void 0 ? void 0 : h.firstWeekContainsDate) !== null && i !== void 0 ? i : 1);
    if (!(w >= 1 && w <= 7))
        throw new RangeError("firstWeekContainsDate must be between 1 and 7 inclusively");
    var S = B((g = (P = (F = (N = t == null ? void 0 : t.weekStartsOn) !== null && N !== void 0 ? N : t == null || (U = t.locale) === null || U === void 0 || (X = U.options) === null || X === void 0 ? void 0 : X.weekStartsOn) !== null && F !== void 0 ? F : G.weekStartsOn) !== null && P !== void 0 ? P : (V = G.locale) === null || V === void 0 || (Q = V.options) === null || Q === void 0 ? void 0 : Q.weekStartsOn) !== null && g !== void 0 ? g : 0);
    if (!(S >= 0 && S <= 6))
        throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");
    if (!m.localize)
        throw new RangeError("locale must contain localize property");
    if (!m.formatLong)
        throw new RangeError("locale must contain formatLong property");
    var O = T(r);
    if (!We(O))
        throw new RangeError("Invalid time value");
    var ae = ze(O)
      , Ce = je(O, ae)
      , Me = {
        firstWeekContainsDate: w,
        weekStartsOn: S,
        locale: m,
        _originalDate: O
    }
      , xe = re.match(Rt).map(function($) {
        var j = $[0];
        if (j === "p" || j === "P") {
            var z = Je[j];
            return z($, m.formatLong)
        }
        return $
    }).join("").match(Yt).map(function($) {
        if ($ === "''")
            return "'";
        var j = $[0];
        if (j === "'")
            return qt($);
        var z = Xe[j];
        if (z)
            return !(t != null && t.useAdditionalWeekYearTokens) && tt($) && he($, e, String(r)),
            !(t != null && t.useAdditionalDayOfYearTokens) && et($) && he($, e, String(r)),
            z(Ce, $, m.localize, Me);
        if (j.match(Lt))
            throw new RangeError("Format string contains an unescaped latin alphabet character `" + j + "`");
        return $
    }).join("");
    return xe
}
function qt(r) {
    var e = r.match(Bt);
    return e ? e[1].replace(Ft, "'") : r
}
function Ht(r) {
    y(1, arguments);
    var e = T(r);
    return e.setDate(1),
    e.setHours(0, 0, 0, 0),
    e
}
function Xt(r) {
    y(1, arguments);
    var e = T(r)
      , t = e.getMonth();
    return e.setFullYear(e.getFullYear(), t + 1, 0),
    e.setHours(23, 59, 59, 999),
    e
}
function Vt(r, e) {
    var t;
    y(1, arguments);
    var a = r || {}
      , n = T(a.start)
      , i = T(a.end)
      , o = i.getTime();
    if (!(n.getTime() <= o))
        throw new RangeError("Invalid interval");
    var d = []
      , l = n;
    l.setHours(0, 0, 0, 0);
    var c = Number((t = e == null ? void 0 : e.step) !== null && t !== void 0 ? t : 1);
    if (c < 1 || isNaN(c))
        throw new RangeError("`options.step` must be a number greater than 1");
    for (; l.getTime() <= o; )
        d.push(T(l)),
        l.setDate(l.getDate() + c),
        l.setHours(0, 0, 0, 0);
    return d
}
function me(r) {
    y(1, arguments);
    var e = T(r);
    return e.setHours(0, 0, 0, 0),
    e
}
function Qt(r, e) {
    y(2, arguments);
    var t = me(r)
      , a = me(e);
    return t.getTime() === a.getTime()
}
function Jt(r) {
    return y(1, arguments),
    Qt(r, Date.now())
}
const zt = "https://api.micro-tab.ru:9443"
  , Kt = Number({}.VITE_API_TIMEOUT_MS) || 3e4
  , D = zt;
class Zt {
    constructor() {
        le(this, "cache", new Map)
    }
    get(e) {
        const t = this.cache.get(e);
        return t ? Date.now() - t.timestamp > t.ttl ? (this.cache.delete(e),
        null) : t.data : null
    }
    set(e, t, a) {
        this.cache.set(e, {
            data: t,
            timestamp: Date.now(),
            ttl: a
        })
    }
    delete(e) {
        this.cache.delete(e)
    }
    clear() {
        this.cache.clear()
    }
    invalidatePattern(e) {
        const t = new RegExp(e);
        for (const a of this.cache.keys())
            t.test(a) && this.cache.delete(a)
    }
}
const E = new Zt
  , Y = {
    birthdays: "birthdays:all",
    calendarMonth: (r, e) => `calendar:${r}:${e}`,
    birthday: r => `birthday:${r}`,
    responsibles: "responsibles:all",
    responsible: r => `responsible:${r}`
}
  , ve = {
    birthdays: 5 * 60 * 1e3,
    calendarMonth: 60 * 60 * 1e3,
    birthday: 5 * 60 * 1e3,
    responsibles: 5 * 60 * 1e3,
    responsible: 5 * 60 * 1e3
};
function K() {
    var r;
    return typeof window != "undefined" && ((r = window.Telegram) != null && r.WebApp) && window.Telegram.WebApp.initData || null
}
function C(r={}) {
    const e = ie({
        "Content-Type": "application/json"
    }, r)
      , t = K();
    return t && (e["X-Init-Data"] = t),
    e
}
function M(t) {
    return b(this, arguments, function*(r, e={}) {
        const a = e.method || "GET";
        s.info("[API] Request options:", {
            method: a,
            headers: e.headers,
            body: e.body ? typeof e.body == "string" ? e.body.substring(0, 200) + "..." : "[...]" : void 0
        });
        try {
            const n = new AbortController
              , i = setTimeout( () => n.abort(), Kt);
            s.info(`[API] Sending ${a} request to ${r}...`);
            const o = yield fetch(r, ue(ie({}, e), {
                signal: n.signal
            }));
            if (clearTimeout(i),
            s.info(`[API] Response received: ${o.status} ${o.statusText}`),
            !o.ok) {
                if (o.status === 0)
                    throw new Error("CORS error: запрос заблокирован браузером");
                const d = o.clone();
                let l = `HTTP ${o.status}: ${o.statusText}`
                  , c = null;
                try {
                    c = yield d.json(),
                    c.detail ? typeof c.detail == "string" ? l = c.detail : Array.isArray(c.detail) && (l = `Ошибка валидации: ${c.detail.map(f => {
                        const h = f.loc ? f.loc.slice(1).join(".") : "unknown"
                          , g = h === "full_name" ? "ФИО" : h === "company" ? "Компания" : h === "position" ? "Должность" : h === "birth_date" ? "Дата рождения" : h === "comment" ? "Комментарий" : h
                          , P = f.msg || f.message || "Ошибка валидации";
                        return `${g}: ${P}`
                    }
                    ).join("; ")}`) : c.errors && (l = `Ошибка валидации: ${c.errors.map(f => {
                        const h = f.loc ? f.loc.slice(1).join(".") : "unknown"
                          , g = h === "full_name" ? "ФИО" : h === "company" ? "Компания" : h === "position" ? "Должность" : h === "birth_date" ? "Дата рождения" : h === "comment" ? "Комментарий" : h
                          , P = f.msg || f.message || "Ошибка валидации";
                        return `${g}: ${P}`
                    }
                    ).join("; ")}`),
                    o.status === 401 ? l = l || "Ошибка авторизации. Пожалуйста, обновите страницу." : o.status === 403 ? l = l || "Доступ запрещен. У вас нет прав для выполнения этого действия." : o.status === 404 ? l = l || "Ресурс не найден. Возможно, он был удален." : o.status === 422 ? l = l || "Ошибка валидации данных. Проверьте введенные данные." : o.status >= 500 && (l = "Ошибка сервера. Пожалуйста, попробуйте позже."),
                    s.error(`[API] Error response for ${a} ${r}:`, c)
                } catch (p) {
                    s.error(`[API] Error response for ${a} ${r}: ${o.status} ${o.statusText}`)
                }
                throw new Error(l)
            }
            return o
        } catch (n) {
            throw s.error(`[API] ===== Fetch ERROR for ${a} ${r} =====`),
            s.error(`[API] Error type: ${ninstanceof Error ? n.constructor.name : typeof n}`),
            s.error(`[API] Error message: ${ninstanceof Error ? n.message : String(n)}`),
            s.error(`[API] Error stack: ${ninstanceof Error ? n.stack : "N/A"}`),
            n instanceof Error ? n.name === "AbortError" ? new Error("Request timeout: сервер не отвечает") : n.message.includes("Failed to fetch") || n.message.includes("NetworkError") ? (s.error(`[API] Network error - возможно CORS или сеть: ${n.message}`),
            new Error("Network error: не удалось подключиться к серверу. Проверьте подключение к интернету и URL API.")) : n.message.includes("CORS") || n.message.includes("Cross-Origin") ? new Error("Ошибка CORS: проверьте настройки сервера") : n : new Error("Unknown error occurred")
        }
    })
}
const ge = {
    getCalendar(r) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/calendar/${r}`, {
                headers: C()
            })).json()
        })
    },
    getCalendarMonth(r, e) {
        return b(this, null, function*() {
            const t = Y.calendarMonth(r, e)
              , a = E.get(t);
            if (a)
                return a;
            const i = yield(yield M(`${D}/api/calendar/month/${r}/${e}`, {
                headers: C()
            })).json();
            return E.set(t, i, ve.calendarMonth),
            i
        })
    },
    getBirthdays() {
        return b(this, null, function*() {
            const r = Y.birthdays
              , e = E.get(r);
            if (e)
                return e;
            const a = yield(yield M(`${D}/api/panel/birthdays`, {
                headers: C()
            })).json();
            return E.set(r, a, ve.birthdays),
            a
        })
    },
    createBirthday(r) {
        return b(this, null, function*() {
            const e = `${D}/api/panel/birthdays`
              , t = C()
              , a = K();
            s.info(`[API] initData length: ${a ? a.length : 0}`),
            s.info("[API] Headers:", {
                "Content-Type": t["Content-Type"],
                "X-Init-Data": t["X-Init-Data"] ? `${t["X-Init-Data"].substring(0, 20)}...` : "missing"
            });
            const n = yield M(e, {
                method: "POST",
                headers: t,
                body: JSON.stringify(r)
            });
            s.info(`[API] createBirthday response received, status: ${n.status}`);
            const i = yield n.json();
            return E.delete(Y.birthdays),
            E.invalidatePattern("^calendar:"),
            i
        })
    },
    updateBirthday(r, e) {
        return b(this, null, function*() {
            const t = `${D}/api/panel/birthdays/${r}`
              , a = C();
            a["Content-Type"] = "application/json";
            const n = K();
            s.info(`[API] initData length: ${n ? n.length : 0}`),
            s.info("[API] updateBirthday headers:", {
                "Content-Type": a["Content-Type"],
                "X-Init-Data": a["X-Init-Data"] ? `${a["X-Init-Data"].substring(0, 20)}...` : "missing"
            }),
            s.info("[API] Request body:", JSON.stringify(e));
            try {
                s.info(`[API] Sending PUT request to ${t}...`);
                const i = yield M(t, {
                    method: "PUT",
                    headers: a,
                    body: JSON.stringify(e)
                });
                if (s.info(`[API] updateBirthday response received, status: ${i.status}`),
                s.info("[API] updateBirthday response headers:", Object.fromEntries(i.headers.entries())),
                s.info("[API] ===== updateBirthday RESPONSE RECEIVED ====="),
                !i.ok)
                    throw s.error(`[API] updateBirthday received non-ok status: ${i.status} ${i.statusText}`),
                    new Error(`HTTP ${i.status}: ${i.statusText}`);
                if (i.status === 204 || i.status === 205)
                    throw s.warn(`[API] updateBirthday received ${i.status} status with no body`),
                    new Error("Сервер вернул ответ без данных");
                if (i.headers.get("Content-Length") === "0")
                    throw s.warn("[API] updateBirthday received response with Content-Length: 0"),
                    new Error("Сервер вернул пустой ответ");
                s.info("[API] updateBirthday reading response body");
                const d = yield i.json();
                if (s.info("[API] updateBirthday response data:", d),
                !d || typeof d != "object")
                    throw s.error("[API] updateBirthday received invalid response data:", d),
                    new Error("Сервер вернул невалидные данные");
                if (!d.id || !d.full_name)
                    throw s.error("[API] updateBirthday response missing required fields:", d),
                    new Error("Сервер вернул неполные данные");
                return s.info(`[API] updateBirthday success: id=${d.id}, full_name=${d.full_name}`),
                s.info("[API] ===== updateBirthday SUCCESS ====="),
                E.delete(Y.birthdays),
                E.delete(Y.birthday(r)),
                E.invalidatePattern("^calendar:"),
                d
            } catch (i) {
                throw s.error("[API] ===== updateBirthday ERROR ====="),
                s.error("[API] updateBirthday error:", i),
                s.error(`[API] Error type: ${iinstanceof Error ? i.constructor.name : typeof i}`),
                s.error(`[API] Error message: ${iinstanceof Error ? i.message : String(i)}`),
                i instanceof Error && i.stack && s.error("[API] Error stack:", i.stack),
                i
            }
        })
    },
    deleteBirthday(r) {
        return b(this, null, function*() {
            const e = `${D}/api/panel/birthdays/${r}`
              , t = C()
              , a = K();
            s.info(`[API] initData length: ${a ? a.length : 0}`),
            s.info("[API] deleteBirthday headers:", {
                "Content-Type": t["Content-Type"],
                "X-Init-Data": t["X-Init-Data"] ? `${t["X-Init-Data"].substring(0, 20)}...` : "missing"
            });
            try {
                s.info(`[API] Sending DELETE request to ${e}...`);
                const n = yield M(e, {
                    method: "DELETE",
                    headers: t
                });
                if (s.info(`[API] deleteBirthday response received, status: ${n.status}`),
                s.info("[API] deleteBirthday response headers:", Object.fromEntries(n.headers.entries())),
                s.info("[API] ===== deleteBirthday RESPONSE RECEIVED ====="),
                !n.ok)
                    throw s.error(`[API] deleteBirthday received non-ok status: ${n.status} ${n.statusText}`),
                    new Error(`HTTP ${n.status}: ${n.statusText}`);
                if (n.status === 204 || n.status === 205) {
                    s.info(`[API] deleteBirthday received ${n.status} status (no body expected)`),
                    s.info(`[API] deleteBirthday success: birthday ${r} deleted`);
                    return
                }
                const i = n.headers.get("Content-Length");
                if (i && i !== "0") {
                    s.info("[API] deleteBirthday reading response body");
                    const o = yield n.json();
                    s.info("[API] deleteBirthday response data:", o)
                } else if (i === "0") {
                    s.info("[API] deleteBirthday received response with Content-Length: 0");
                    return
                }
                s.info(`[API] deleteBirthday success: birthday ${r} deleted`),
                s.info("[API] ===== deleteBirthday SUCCESS ====="),
                E.delete(Y.birthdays),
                E.delete(Y.birthday(r)),
                E.invalidatePattern("^calendar:"),
                s.info("[API] deleteBirthday completed successfully")
            } catch (n) {
                throw s.error("[API] ===== deleteBirthday ERROR ====="),
                s.error("[API] deleteBirthday error:", n),
                s.error(`[API] Error type: ${ninstanceof Error ? n.constructor.name : typeof n}`),
                s.error(`[API] Error message: ${ninstanceof Error ? n.message : String(n)}`),
                n instanceof Error && n.stack && s.error("[API] Error stack:", n.stack),
                n
            }
        })
    },
    getResponsible() {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/responsible`, {
                headers: C()
            })).json()
        })
    },
    createResponsible(r) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/responsible`, {
                method: "POST",
                headers: C(),
                body: JSON.stringify(r)
            })).json()
        })
    },
    updateResponsible(r, e) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/responsible/${r}`, {
                method: "PUT",
                headers: C(),
                body: JSON.stringify(e)
            })).json()
        })
    },
    deleteResponsible(r) {
        return b(this, null, function*() {
            yield M(`${D}/api/panel/responsible/${r}`, {
                method: "DELETE",
                headers: C()
            })
        })
    },
    assignResponsible(r, e) {
        return b(this, null, function*() {
            yield M(`${D}/api/panel/assign-responsible`, {
                method: "POST",
                headers: C(),
                body: JSON.stringify({
                    responsible_id: r,
                    date: e
                })
            })
        })
    },
    searchPeople(r) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/search?q=${encodeURIComponent(r)}`, {
                headers: C()
            })).json()
        })
    },
    generateGreeting(r, e, t, a) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/generate-greeting`, {
                method: "POST",
                headers: C(),
                body: JSON.stringify({
                    birthday_id: r,
                    style: e,
                    length: t,
                    theme: a
                })
            })).json()
        })
    },
    createCard(r, e, t) {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/create-card`, {
                method: "POST",
                headers: C(),
                body: JSON.stringify({
                    birthday_id: r,
                    greeting_text: e,
                    qr_url: t
                })
            })).blob()
        })
    },
    checkPanelAccess() {
        return b(this, null, function*() {
            return (yield M(`${D}/api/panel/check-access`, {
                headers: C()
            })).json()
        })
    }
};
function J(r, e) {
    if (r.one !== void 0 && e === 1)
        return r.one;
    var t = e % 10
      , a = e % 100;
    return t === 1 && a !== 11 ? r.singularNominative.replace("{{count}}", String(e)) : t >= 2 && t <= 4 && (a < 10 || a > 20) ? r.singularGenitive.replace("{{count}}", String(e)) : r.pluralGenitive.replace("{{count}}", String(e))
}
function x(r) {
    return function(e, t) {
        return t != null && t.addSuffix ? t.comparison && t.comparison > 0 ? r.future ? J(r.future, e) : "через " + J(r.regular, e) : r.past ? J(r.past, e) : J(r.regular, e) + " назад" : J(r.regular, e)
    }
}
var er = {
    lessThanXSeconds: x({
        regular: {
            one: "меньше секунды",
            singularNominative: "меньше {{count}} секунды",
            singularGenitive: "меньше {{count}} секунд",
            pluralGenitive: "меньше {{count}} секунд"
        },
        future: {
            one: "меньше, чем через секунду",
            singularNominative: "меньше, чем через {{count}} секунду",
            singularGenitive: "меньше, чем через {{count}} секунды",
            pluralGenitive: "меньше, чем через {{count}} секунд"
        }
    }),
    xSeconds: x({
        regular: {
            singularNominative: "{{count}} секунда",
            singularGenitive: "{{count}} секунды",
            pluralGenitive: "{{count}} секунд"
        },
        past: {
            singularNominative: "{{count}} секунду назад",
            singularGenitive: "{{count}} секунды назад",
            pluralGenitive: "{{count}} секунд назад"
        },
        future: {
            singularNominative: "через {{count}} секунду",
            singularGenitive: "через {{count}} секунды",
            pluralGenitive: "через {{count}} секунд"
        }
    }),
    halfAMinute: function(e, t) {
        return t != null && t.addSuffix ? t.comparison && t.comparison > 0 ? "через полминуты" : "полминуты назад" : "полминуты"
    },
    lessThanXMinutes: x({
        regular: {
            one: "меньше минуты",
            singularNominative: "меньше {{count}} минуты",
            singularGenitive: "меньше {{count}} минут",
            pluralGenitive: "меньше {{count}} минут"
        },
        future: {
            one: "меньше, чем через минуту",
            singularNominative: "меньше, чем через {{count}} минуту",
            singularGenitive: "меньше, чем через {{count}} минуты",
            pluralGenitive: "меньше, чем через {{count}} минут"
        }
    }),
    xMinutes: x({
        regular: {
            singularNominative: "{{count}} минута",
            singularGenitive: "{{count}} минуты",
            pluralGenitive: "{{count}} минут"
        },
        past: {
            singularNominative: "{{count}} минуту назад",
            singularGenitive: "{{count}} минуты назад",
            pluralGenitive: "{{count}} минут назад"
        },
        future: {
            singularNominative: "через {{count}} минуту",
            singularGenitive: "через {{count}} минуты",
            pluralGenitive: "через {{count}} минут"
        }
    }),
    aboutXHours: x({
        regular: {
            singularNominative: "около {{count}} часа",
            singularGenitive: "около {{count}} часов",
            pluralGenitive: "около {{count}} часов"
        },
        future: {
            singularNominative: "приблизительно через {{count}} час",
            singularGenitive: "приблизительно через {{count}} часа",
            pluralGenitive: "приблизительно через {{count}} часов"
        }
    }),
    xHours: x({
        regular: {
            singularNominative: "{{count}} час",
            singularGenitive: "{{count}} часа",
            pluralGenitive: "{{count}} часов"
        }
    }),
    xDays: x({
        regular: {
            singularNominative: "{{count}} день",
            singularGenitive: "{{count}} дня",
            pluralGenitive: "{{count}} дней"
        }
    }),
    aboutXWeeks: x({
        regular: {
            singularNominative: "около {{count}} недели",
            singularGenitive: "около {{count}} недель",
            pluralGenitive: "около {{count}} недель"
        },
        future: {
            singularNominative: "приблизительно через {{count}} неделю",
            singularGenitive: "приблизительно через {{count}} недели",
            pluralGenitive: "приблизительно через {{count}} недель"
        }
    }),
    xWeeks: x({
        regular: {
            singularNominative: "{{count}} неделя",
            singularGenitive: "{{count}} недели",
            pluralGenitive: "{{count}} недель"
        }
    }),
    aboutXMonths: x({
        regular: {
            singularNominative: "около {{count}} месяца",
            singularGenitive: "около {{count}} месяцев",
            pluralGenitive: "около {{count}} месяцев"
        },
        future: {
            singularNominative: "приблизительно через {{count}} месяц",
            singularGenitive: "приблизительно через {{count}} месяца",
            pluralGenitive: "приблизительно через {{count}} месяцев"
        }
    }),
    xMonths: x({
        regular: {
            singularNominative: "{{count}} месяц",
            singularGenitive: "{{count}} месяца",
            pluralGenitive: "{{count}} месяцев"
        }
    }),
    aboutXYears: x({
        regular: {
            singularNominative: "около {{count}} года",
            singularGenitive: "около {{count}} лет",
            pluralGenitive: "около {{count}} лет"
        },
        future: {
            singularNominative: "приблизительно через {{count}} год",
            singularGenitive: "приблизительно через {{count}} года",
            pluralGenitive: "приблизительно через {{count}} лет"
        }
    }),
    xYears: x({
        regular: {
            singularNominative: "{{count}} год",
            singularGenitive: "{{count}} года",
            pluralGenitive: "{{count}} лет"
        }
    }),
    overXYears: x({
        regular: {
            singularNominative: "больше {{count}} года",
            singularGenitive: "больше {{count}} лет",
            pluralGenitive: "больше {{count}} лет"
        },
        future: {
            singularNominative: "больше, чем через {{count}} год",
            singularGenitive: "больше, чем через {{count}} года",
            pluralGenitive: "больше, чем через {{count}} лет"
        }
    }),
    almostXYears: x({
        regular: {
            singularNominative: "почти {{count}} год",
            singularGenitive: "почти {{count}} года",
            pluralGenitive: "почти {{count}} лет"
        },
        future: {
            singularNominative: "почти через {{count}} год",
            singularGenitive: "почти через {{count}} года",
            pluralGenitive: "почти через {{count}} лет"
        }
    })
}
  , tr = function(e, t, a) {
    return er[e](t, a)
};
const rr = tr;
var ar = {
    full: "EEEE, d MMMM y 'г.'",
    long: "d MMMM y 'г.'",
    medium: "d MMM y 'г.'",
    short: "dd.MM.y"
}
  , nr = {
    full: "H:mm:ss zzzz",
    long: "H:mm:ss z",
    medium: "H:mm:ss",
    short: "H:mm"
}
  , ir = {
    any: "{{date}}, {{time}}"
}
  , or = {
    date: q({
        formats: ar,
        defaultWidth: "full"
    }),
    time: q({
        formats: nr,
        defaultWidth: "full"
    }),
    dateTime: q({
        formats: ir,
        defaultWidth: "any"
    })
};
const sr = or;
function ye(r, e, t) {
    y(2, arguments);
    var a = H(r, t)
      , n = H(e, t);
    return a.getTime() === n.getTime()
}
var oe = ["воскресенье", "понедельник", "вторник", "среду", "четверг", "пятницу", "субботу"];
function ur(r) {
    var e = oe[r];
    switch (r) {
    case 0:
        return "'в прошлое " + e + " в' p";
    case 1:
    case 2:
    case 4:
        return "'в прошлый " + e + " в' p";
    case 3:
    case 5:
    case 6:
        return "'в прошлую " + e + " в' p"
    }
}
function pe(r) {
    var e = oe[r];
    return r === 2 ? "'во " + e + " в' p" : "'в " + e + " в' p"
}
function lr(r) {
    var e = oe[r];
    switch (r) {
    case 0:
        return "'в следующее " + e + " в' p";
    case 1:
    case 2:
    case 4:
        return "'в следующий " + e + " в' p";
    case 3:
    case 5:
    case 6:
        return "'в следующую " + e + " в' p"
    }
}
var dr = {
    lastWeek: function(e, t, a) {
        var n = e.getUTCDay();
        return ye(e, t, a) ? pe(n) : ur(n)
    },
    yesterday: "'вчера в' p",
    today: "'сегодня в' p",
    tomorrow: "'завтра в' p",
    nextWeek: function(e, t, a) {
        var n = e.getUTCDay();
        return ye(e, t, a) ? pe(n) : lr(n)
    },
    other: "P"
}
  , cr = function(e, t, a, n) {
    var i = dr[e];
    return typeof i == "function" ? i(t, a, n) : i
};
const fr = cr;
var hr = {
    narrow: ["до н.э.", "н.э."],
    abbreviated: ["до н. э.", "н. э."],
    wide: ["до нашей эры", "нашей эры"]
}
  , mr = {
    narrow: ["1", "2", "3", "4"],
    abbreviated: ["1-й кв.", "2-й кв.", "3-й кв.", "4-й кв."],
    wide: ["1-й квартал", "2-й квартал", "3-й квартал", "4-й квартал"]
}
  , vr = {
    narrow: ["Я", "Ф", "М", "А", "М", "И", "И", "А", "С", "О", "Н", "Д"],
    abbreviated: ["янв.", "фев.", "март", "апр.", "май", "июнь", "июль", "авг.", "сент.", "окт.", "нояб.", "дек."],
    wide: ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
}
  , gr = {
    narrow: ["Я", "Ф", "М", "А", "М", "И", "И", "А", "С", "О", "Н", "Д"],
    abbreviated: ["янв.", "фев.", "мар.", "апр.", "мая", "июн.", "июл.", "авг.", "сент.", "окт.", "нояб.", "дек."],
    wide: ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
}
  , yr = {
    narrow: ["В", "П", "В", "С", "Ч", "П", "С"],
    short: ["вс", "пн", "вт", "ср", "чт", "пт", "сб"],
    abbreviated: ["вск", "пнд", "втр", "срд", "чтв", "птн", "суб"],
    wide: ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
}
  , pr = {
    narrow: {
        am: "ДП",
        pm: "ПП",
        midnight: "полн.",
        noon: "полд.",
        morning: "утро",
        afternoon: "день",
        evening: "веч.",
        night: "ночь"
    },
    abbreviated: {
        am: "ДП",
        pm: "ПП",
        midnight: "полн.",
        noon: "полд.",
        morning: "утро",
        afternoon: "день",
        evening: "веч.",
        night: "ночь"
    },
    wide: {
        am: "ДП",
        pm: "ПП",
        midnight: "полночь",
        noon: "полдень",
        morning: "утро",
        afternoon: "день",
        evening: "вечер",
        night: "ночь"
    }
}
  , wr = {
    narrow: {
        am: "ДП",
        pm: "ПП",
        midnight: "полн.",
        noon: "полд.",
        morning: "утра",
        afternoon: "дня",
        evening: "веч.",
        night: "ночи"
    },
    abbreviated: {
        am: "ДП",
        pm: "ПП",
        midnight: "полн.",
        noon: "полд.",
        morning: "утра",
        afternoon: "дня",
        evening: "веч.",
        night: "ночи"
    },
    wide: {
        am: "ДП",
        pm: "ПП",
        midnight: "полночь",
        noon: "полдень",
        morning: "утра",
        afternoon: "дня",
        evening: "вечера",
        night: "ночи"
    }
}
  , br = function(e, t) {
    var a = Number(e), n = t == null ? void 0 : t.unit, i;
    return n === "date" ? i = "-е" : n === "week" || n === "minute" || n === "second" ? i = "-я" : i = "-й",
    a + i
}
  , Pr = {
    ordinalNumber: br,
    era: W({
        values: hr,
        defaultWidth: "wide"
    }),
    quarter: W({
        values: mr,
        defaultWidth: "wide",
        argumentCallback: function(e) {
            return e - 1
        }
    }),
    month: W({
        values: vr,
        defaultWidth: "wide",
        formattingValues: gr,
        defaultFormattingWidth: "wide"
    }),
    day: W({
        values: yr,
        defaultWidth: "wide"
    }),
    dayPeriod: W({
        values: pr,
        defaultWidth: "any",
        formattingValues: wr,
        defaultFormattingWidth: "wide"
    })
};
const Tr = Pr;
var Dr = /^(\d+)(-?(е|я|й|ое|ье|ая|ья|ый|ой|ий|ый))?/i
  , Cr = /\d+/i
  , Mr = {
    narrow: /^((до )?н\.?\s?э\.?)/i,
    abbreviated: /^((до )?н\.?\s?э\.?)/i,
    wide: /^(до нашей эры|нашей эры|наша эра)/i
}
  , xr = {
    any: [/^д/i, /^н/i]
}
  , $r = {
    narrow: /^[1234]/i,
    abbreviated: /^[1234](-?[ыои]?й?)? кв.?/i,
    wide: /^[1234](-?[ыои]?й?)? квартал/i
}
  , Sr = {
    any: [/1/i, /2/i, /3/i, /4/i]
}
  , Er = {
    narrow: /^[яфмаисонд]/i,
    abbreviated: /^(янв|фев|март?|апр|ма[йя]|июн[ья]?|июл[ья]?|авг|сент?|окт|нояб?|дек)\.?/i,
    wide: /^(январ[ья]|феврал[ья]|марта?|апрел[ья]|ма[йя]|июн[ья]|июл[ья]|августа?|сентябр[ья]|октябр[ья]|октябр[ья]|ноябр[ья]|декабр[ья])/i
}
  , Or = {
    narrow: [/^я/i, /^ф/i, /^м/i, /^а/i, /^м/i, /^и/i, /^и/i, /^а/i, /^с/i, /^о/i, /^н/i, /^я/i],
    any: [/^я/i, /^ф/i, /^мар/i, /^ап/i, /^ма[йя]/i, /^июн/i, /^июл/i, /^ав/i, /^с/i, /^о/i, /^н/i, /^д/i]
}
  , kr = {
    narrow: /^[впсч]/i,
    short: /^(вс|во|пн|по|вт|ср|чт|че|пт|пя|сб|су)\.?/i,
    abbreviated: /^(вск|вос|пнд|пон|втр|вто|срд|сре|чтв|чет|птн|пят|суб).?/i,
    wide: /^(воскресень[ея]|понедельника?|вторника?|сред[аы]|четверга?|пятниц[аы]|суббот[аы])/i
}
  , Nr = {
    narrow: [/^в/i, /^п/i, /^в/i, /^с/i, /^ч/i, /^п/i, /^с/i],
    any: [/^в[ос]/i, /^п[он]/i, /^в/i, /^ср/i, /^ч/i, /^п[ят]/i, /^с[уб]/i]
}
  , Wr = {
    narrow: /^([дп]п|полн\.?|полд\.?|утр[оа]|день|дня|веч\.?|ноч[ьи])/i,
    abbreviated: /^([дп]п|полн\.?|полд\.?|утр[оа]|день|дня|веч\.?|ноч[ьи])/i,
    wide: /^([дп]п|полночь|полдень|утр[оа]|день|дня|вечера?|ноч[ьи])/i
}
  , Ir = {
    any: {
        am: /^дп/i,
        pm: /^пп/i,
        midnight: /^полн/i,
        noon: /^полд/i,
        morning: /^у/i,
        afternoon: /^д[ен]/i,
        evening: /^в/i,
        night: /^н/i
    }
}
  , jr = {
    ordinalNumber: De({
        matchPattern: Dr,
        parsePattern: Cr,
        valueCallback: function(e) {
            return parseInt(e, 10)
        }
    }),
    era: I({
        matchPatterns: Mr,
        defaultMatchWidth: "wide",
        parsePatterns: xr,
        defaultParseWidth: "any"
    }),
    quarter: I({
        matchPatterns: $r,
        defaultMatchWidth: "wide",
        parsePatterns: Sr,
        defaultParseWidth: "any",
        valueCallback: function(e) {
            return e + 1
        }
    }),
    month: I({
        matchPatterns: Er,
        defaultMatchWidth: "wide",
        parsePatterns: Or,
        defaultParseWidth: "any"
    }),
    day: I({
        matchPatterns: kr,
        defaultMatchWidth: "wide",
        parsePatterns: Nr,
        defaultParseWidth: "any"
    }),
    dayPeriod: I({
        matchPatterns: Wr,
        defaultMatchWidth: "wide",
        parsePatterns: Ir,
        defaultParseWidth: "any"
    })
};
const _r = jr;
var Ar = {
    code: "ru",
    formatDistance: rr,
    formatLong: sr,
    formatRelative: fr,
    localize: Tr,
    match: _r,
    options: {
        weekStartsOn: 1,
        firstWeekContainsDate: 1
    }
};
const we = Ar;
function Ur({date: r, data: e, loading: t, error: a}) {
    if (t)
        return u.jsx("div", {
            className: "date-view",
            children: "Загрузка..."
        });
    const n = i => {
        const o = A(i, "d MMMM yyyy", {
            locale: we
        })
          , d = A(i, "EEEE", {
            locale: we
        });
        return `${o}, ${d}`
    }
    ;
    return a ? u.jsxs("div", {
        className: "date-view",
        children: [u.jsx("h3", {
            children: n(r)
        }), u.jsxs("div", {
            className: "error-message",
            children: [u.jsx("p", {
                children: "⚠️ Ошибка загрузки данных"
            }), u.jsx("p", {
                children: a
            }), u.jsx("p", {
                className: "error-hint",
                children: "Проверьте подключение к интернету и настройки API."
            })]
        })]
    }) : e ? u.jsxs("div", {
        className: "date-view",
        children: [u.jsx("h3", {
            children: n(r)
        }), u.jsxs("div", {
            className: "date-section",
            children: [u.jsx("h4", {
                children: "🎂 Дни рождения"
            }), e.birthdays.length > 0 ? e.birthdays.map(i => u.jsxs("div", {
                className: "birthday-item",
                children: [u.jsx("p", {
                    children: u.jsx("strong", {
                        children: i.full_name
                    })
                }), u.jsxs("p", {
                    children: [i.company, ", ", i.position]
                }), u.jsxs("p", {
                    children: ["Исполняется ", i.age, " лет"]
                }), i.comment && u.jsxs("p", {
                    className: "comment",
                    children: ["Комментарий: ", i.comment]
                })]
            }, i.id)) : u.jsx("p", {
                style: {
                    color: "#666",
                    fontStyle: "italic"
                },
                children: "Нет дней рождения на эту дату"
            })]
        }), u.jsxs("div", {
            className: "date-section",
            children: [u.jsx("h4", {
                children: "🎉 Профессиональные праздники"
            }), e.holidays.length > 0 ? e.holidays.map(i => u.jsxs("div", {
                className: "holiday-item",
                children: [u.jsx("p", {
                    children: u.jsx("strong", {
                        children: i.name
                    })
                }), i.description && u.jsx("p", {
                    children: i.description
                })]
            }, i.id)) : u.jsx("p", {
                style: {
                    color: "#666",
                    fontStyle: "italic"
                },
                children: "Нет профессиональных праздников"
            })]
        }), u.jsxs("div", {
            className: "date-section",
            children: [u.jsx("h4", {
                children: "👤 Ответственное лицо"
            }), e.responsible ? u.jsxs("div", {
                className: "responsible-item",
                children: [u.jsx("p", {
                    children: u.jsx("strong", {
                        children: e.responsible.full_name
                    })
                }), u.jsxs("p", {
                    children: [e.responsible.company, ", ", e.responsible.position]
                })]
            }) : u.jsx("p", {
                style: {
                    color: "#666",
                    fontStyle: "italic"
                },
                children: "Ответственный не назначен"
            })]
        })]
    }) : u.jsxs("div", {
        className: "date-view",
        children: [u.jsx("h3", {
            children: n(r)
        }), u.jsx("p", {
            children: "Нет данных для этой даты"
        })]
    })
}
const Gr = k.memo(Ur);
function Br() {
    const [r,e] = k.useState(new Date)
      , [t,a] = k.useState(null)
      , [n,i] = k.useState(null)
      , [o,d] = k.useState(!1)
      , [l,c] = k.useState(null)
      , [p,f] = k.useState(null)
      , [h,g] = k.useState(null)
      , [,P] = k.useState(!1);
    k.useEffect( () => {}
    , []),
    k.useEffect( () => {
        ( () => b(this, null, function*() {
            const w = r.getFullYear()
              , S = r.getMonth() + 1;
            P(!0);
            try {
                const O = yield ge.getCalendarMonth(w, S);
                g(O)
            } catch (O) {
                s.error("[Calendar] Failed to load month birthdays:", O),
                g(null)
            } finally {
                P(!1)
            }
        }))()
    }
    , [r]);
    const N = ( () => {
        try {
            const m = Ht(r)
              , w = Xt(r);
            return Vt({
                start: m,
                end: w
            })
        } catch (m) {
            return s.error("[Calendar] Error calculating month days:", m),
            f("Ошибка при отображении календаря. Попробуйте обновить страницу."),
            [new Date]
        }
    }
    )()
      , U = m => {
        if (!h)
            return !1;
        const w = A(m, "yyyy-MM-dd");
        return w in h.birthdays_by_date && h.birthdays_by_date[w].length > 0
    }
      , X = m => t ? A(m, "yyyy-MM-dd") === A(t, "yyyy-MM-dd") : !1
      , V = m => Jt(m)
      , Q = m => b(this, null, function*() {
        try {
            a(m),
            d(!0),
            c(null),
            i(null);
            const w = A(m, "yyyy-MM-dd")
              , S = yield ge.getCalendar(w);
            i(S),
            c(null)
        } catch (w) {
            s.error("[Calendar] Failed to load calendar data:", w);
            const S = w instanceof Error ? w.message : "Не удалось загрузить данные";
            c(S),
            i(null)
        } finally {
            d(!1)
        }
    })
      , re = () => {
        e(new Date(r.getFullYear(),r.getMonth() - 1,1)),
        a(null),
        i(null)
    }
      , G = () => {
        e(new Date(r.getFullYear(),r.getMonth() + 1,1)),
        a(null),
        i(null)
    }
    ;
    return p ? u.jsx("div", {
        className: "calendar-container",
        children: u.jsxs("div", {
            className: "error-message",
            style: {
                padding: "20px",
                textAlign: "center"
            },
            children: [u.jsxs("p", {
                children: ["⚠️ ", p]
            }), u.jsx("button", {
                onClick: () => {
                    f(null),
                    e(new Date)
                }
                ,
                style: {
                    marginTop: "10px",
                    padding: "10px 20px",
                    background: "#007bff",
                    color: "white",
                    border: "none",
                    borderRadius: "4px",
                    cursor: "pointer"
                },
                children: "Обновить календарь"
            })]
        })
    }) : u.jsxs("div", {
        className: "calendar-container",
        children: [u.jsxs("div", {
            className: "calendar-header",
            children: [u.jsx("button", {
                onClick: re,
                children: "◀️"
            }), u.jsx("h2", {
                children: A(r, "MMMM yyyy")
            }), u.jsx("button", {
                onClick: G,
                children: "▶️"
            })]
        }), u.jsxs("div", {
            className: "calendar-grid",
            children: [["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"].map(m => u.jsx("div", {
                className: "calendar-day-header",
                children: m
            }, m)), N.length > 0 ? N.map(m => {
                const w = U(m)
                  , S = X(m)
                  , O = V(m)
                  , ae = ["calendar-day", S ? "selected" : "", O ? "today" : "", w ? "has-birthday" : ""].filter(Boolean).join(" ");
                return u.jsxs("button", {
                    className: ae,
                    onClick: () => Q(m),
                    title: w ? "Есть дни рождения" : O ? "Сегодня" : "",
                    children: [u.jsx("span", {
                        className: "day-number",
                        children: A(m, "d")
                    }), w && u.jsx("span", {
                        className: "birthday-indicator",
                        children: "🎂"
                    })]
                }, m.toISOString())
            }
            ) : u.jsx("div", {
                style: {
                    gridColumn: "1 / -1",
                    textAlign: "center",
                    padding: "20px"
                },
                children: u.jsx("p", {
                    children: "Не удалось загрузить календарь"
                })
            })]
        }), t && u.jsx(Gr, {
            date: t,
            data: n,
            loading: o,
            error: l
        })]
    })
}
export {Br as default};


.calendar-container {
    padding: 20px;
    max-width: 600px;
    margin: 0 auto
}

.calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px
}

.calendar-header button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    padding: 5px 15px
}

.calendar-header h2 {
    font-size: 20px;
    font-weight: 600
}

.calendar-grid {
    display: grid;
    grid-template-columns: repeat(7,1fr);
    gap: 5px;
    margin-bottom: 20px
}

.calendar-day-header {
    text-align: center;
    font-weight: 600;
    padding: 10px;
    background-color: #f0f0f0
}

.calendar-day {
    padding: 10px;
    border: 2px solid #ddd;
    background: white;
    cursor: pointer;
    text-align: center;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 50px;
    transition: all .2s ease
}

.calendar-day:hover {
    background-color: #f0f0f0;
    border-color: #007bff;
    transform: scale(1.05)
}

.calendar-day.selected {
    background-color: #007bff;
    color: #fff;
    border-color: #0056b3;
    box-shadow: 0 2px 8px #007bff66;
    font-weight: 700
}

.calendar-day.selected:hover {
    background-color: #0056b3;
    transform: scale(1.05)
}

.calendar-day.has-birthday {
    border-color: #ffc107;
    background: linear-gradient(to bottom,#fff9e6 0%,#ffffff 100%)
}

.calendar-day.has-birthday:hover {
    background: linear-gradient(to bottom,#fff3cd 0%,#fff9e6 100%);
    border-color: #ff9800
}

.calendar-day.selected.has-birthday {
    background: linear-gradient(to bottom,#0056b3 0%,#007bff 100%);
    border-color: #004085
}

.calendar-day.today {
    border-color: #28a745;
    border-width: 3px;
    font-weight: 700
}

.calendar-day.today:not(.selected) {
    background: linear-gradient(to bottom,#d4edda 0%,#ffffff 100%)
}

.calendar-day.today.has-birthday:not(.selected) {
    background: linear-gradient(to bottom,#fff3cd 0%,#d4edda 50%,#ffffff 100%);
    border-color: #ffc107
}

.calendar-day.today.selected {
    border-color: #0056b3;
    box-shadow: 0 2px 8px #007bff66,0 0 0 2px #28a7454d
}

.calendar-day .day-number {
    font-size: 16px;
    line-height: 1.2
}

.calendar-day .birthday-indicator {
    font-size: 12px;
    margin-top: 2px;
    line-height: 1
}

.calendar-day.selected .birthday-indicator {
    filter: brightness(0) invert(1)
}

.date-view {
    margin-top: 20px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px
}

.date-view h3 {
    margin-bottom: 15px;
    font-size: 18px
}

.date-section {
    margin-bottom: 20px
}

.date-section h4 {
    margin-bottom: 10px;
    font-size: 16px
}

.birthday-item,.holiday-item,.responsible-item {
    padding: 10px;
    margin-bottom: 10px;
    background: white;
    border-radius: 4px
}

.birthday-item p,.holiday-item p,.responsible-item p {
    margin: 5px 0
}

.comment {
    font-style: italic;
    color: #666
}

.error-message {
    padding: 20px;
    text-align: center;
    background-color: #fff3cd;
    border: 1px solid #ffc107;
    border-radius: 8px;
    color: #856404
}

.error-message p {
    margin: 0 0 10px;
    font-size: 16px
}
