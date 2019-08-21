using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;

class Scanner
{
    string[] s;
    int i;

    char[] cs = new char[] { ' ' };

    public Scanner()
    {
        s = new string[0];
        i = 0;
    }

    public string next()
    {
        if (i < s.Length) return s[i++];
        string st = Console.ReadLine();
        while (st == "") st = Console.ReadLine();
        s = st.Split(cs, StringSplitOptions.RemoveEmptyEntries);
        if (s.Length == 0) return next();
        i = 0;
        return s[i++];
    }

    public int nextInt()
    {
        return int.Parse(next());
    }
    public int[] ArrayInt(int N, int add = 0)
    {
        int[] Array = new int[N];
        for (int i = 0; i < N; i++)
        {
            Array[i] = nextInt() + add;
        }
        return Array;
    }

    public long nextLong()
    {
        return long.Parse(next());
    }

    public long[] ArrayLong(int N, long add = 0)
    {
        long[] Array = new long[N];
        for (int i = 0; i < N; i++)
        {
            Array[i] = nextLong() + add;
        }
        return Array;
    }

    public double nextDouble()
    {
        return double.Parse(next());
    }

    public double[] ArrayDouble(int N, double add = 0)
    {
        double[] Array = new double[N];
        for (int i = 0; i < N; i++)
        {
            Array[i] = nextDouble() + add;
        }
        return Array;
    }
}

class Myon
{
    public Myon() { }
    public static int Main()
    {
        cin = new Scanner();
        new Myon().calc();
        return 0;
    }

    void calc()
    {
        cin = new Scanner();

        long N = cin.nextLong();
        long C = cin.nextLong();

        var chanels = new (long, long, long)[N];

        for(long i = 0; i < N; i++) {
            long s = cin.nextLong();
            long t = cin.nextLong();
            long c = cin.nextLong();
            chanels[i] = (s, t, c);
        }

        Array.Sort(chanels, (a, b) => {
            var ret = a.Item3.CompareTo(b.Item3);

            return ret != 0 ? ret : a.Item2.CompareTo(b.Item2);
        });
        long T = 220000;
        long[] imos = new long[T];

        var prev = (0L, 0L, -1L);  // s, t, c

        for(long i = 0; i < N; i++) {
            long s = chanels[i].Item1;
            long t = chanels[i].Item2;
            long c = chanels[i].Item3;

            if(c == prev.Item3 && s == prev.Item1) {
                prev.Item2 = t;
            } else {
                if(prev.Item3 != -1) {
                    imos[prev.Item1 * 2] += 1;
                    imos[prev.Item2 * 2 + 1] -= 1;
                }
                prev = (s, t, c);
            }
        }

        imos[prev.Item1 * 2] += 1;
        imos[prev.Item2 * 2 + 1] -= 1;

        long ans = 0;
        long now = 0;
        for(long i = 0; i < T; i ++) {
            now += imos[i];
            ans = Math.Max(now, ans);
        }
        Console.WriteLine(ans);
    }

    static Scanner cin;
}
